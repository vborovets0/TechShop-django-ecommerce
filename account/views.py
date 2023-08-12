from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib import messages

from .forms import RegistrationForm, UserEditForm, UserAddressForm
from .models import UserBase, Address
from .token import account_activation_token


@login_required
def dashboard(request):
    # orders = user_orders(request)
    return render(request, 'account/user/dashboard.html',)


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')


def account_registration(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(subject, message, to=[user.email])
            email.send()
            if email.send():
                messages.success(request, f"Please go to your email {user.email}"
                                          f" and click in activation link to confirm the registration.")

            else:
                messages.error(request, f"Problem sending email to {user.email},"
                                        f"check if you typed it correctly")
            return redirect("/")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserBase.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')

# Addresses


@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    return render(request, "account/dashboard/addresses.html", {"addresses": addresses})


@login_required
def add_address(request):
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            address_form.save()
            return HttpResponseRedirect(reverse("account:addresses"))
    else:
        address_form = UserAddressForm()
    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})


@login_required
def edit_address(request, id):
    if request.method == "POST":
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address, data=request.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse("account:addresses"))
    else:
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address)
    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})


@login_required
def delete_address(request, id):
    address = Address.objects.filter(pk=id, customer=request.user).delete()
    return redirect("account:addresses")


@login_required
def set_default(request, id):
    Address.objects.filter(customer=request.user, default=True).update(default=False)
    Address.objects.filter(pk=id, customer=request.user).update(default=True)

    previous_url = request.META.get("HTTP_REFERER")

    if "delivery_address" in previous_url:
        return redirect("checkout:delivery_address")

    return redirect("account:addresses")


