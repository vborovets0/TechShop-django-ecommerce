import factory

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


