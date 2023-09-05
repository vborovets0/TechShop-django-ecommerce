import factory
from factory import Factory

from account.models import UserBase, Address
from basket.basket import Basket
from shop.models import Category, Product
from faker import Faker

fake = Faker()


# Shop
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category {n}')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f'Product {n}')
    description = 'Test description'
    category = factory.SubFactory(CategoryFactory)
    price = 10.0
    in_stock = True
    is_active = True


class UserBaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserBase

    email = "user@base.com"
    user_name = "username"
    password = "userpassword"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    user = factory.SubFactory(UserBaseFactory)
    full_name = fake.name()
    phone = fake.phone_number()
    postcode = fake.postcode()
    address_line = fake.street_address()
    address_line2 = fake.street_address()
    town_city = fake.city_suffix


class BasketFactory(Factory):
    class Meta:
        model = Basket

    request = None

