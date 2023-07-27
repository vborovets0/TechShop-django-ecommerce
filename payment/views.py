from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def BasketView(request):

    # basket = Basket(request)
    # total = str(basket.get_total_price())
    # total = total.replace('.', '')
    # total = int(total)
    #
    # stripe.api_key = ''
    # intent = stripe.PaymentIntent.create(
    #     amount=total,
    #     currency='gbp',
    #     metadata={'userid': request.user.id}
    # )

    return render(request, 'payment/home.html')
                  # {'client_secret': intent.client_secret})

