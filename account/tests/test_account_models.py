import pytest


def test_user_str(userbase):
    assert str(userbase) == userbase.user_name


def test_adminuser_str(adminuser):
    assert str(adminuser) == adminuser.user_name


def test_user_email_no_input(user_base_factory):
    with pytest.raises(ValueError) as e:
        test = user_base_factory.create(email="")
    assert str(e.value) == "You must provide an email address"


@pytest.mark.django_db
def test_user_email_incorrect(user_base_factory):
    with pytest.raises(ValueError) as e:
        test = user_base_factory.create(email="email.com")
    assert str(e.value) == "You must provide a valid email address"


def test_adminuser_email_not_staff(user_base_factory):
    with pytest.raises(ValueError) as e:
        test = user_base_factory.create(email="", is_superuser=True, is_staff=False)
    assert str(e.value) == "Superuser must be assigned to is_staff=True."


def test_adminuser_email_not_superuser(user_base_factory):
    with pytest.raises(ValueError) as e:
        test = user_base_factory.create(email="email.com", is_superuser=False, is_staff=True)
    assert str(e.value) == "Superuser must be assigned to is_superuser=True."


def test_address_str(address):
    assert str(address) == "Address"