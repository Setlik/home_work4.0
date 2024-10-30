import pytest

from src.products import Category, Product


@pytest.fixture
def sample_product():
    return Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0,
                   quantity=5)


@pytest.fixture
def sample_category(sample_product):
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    products=[sample_product])


@pytest.fixture
def test_product():
    product_a = Product(name='Товар A', description='Описание A', price=100.0, quantity=10)
    product_b = Product(name='Товар B', description='Описание B', price=200.0, quantity=2)
    product_c = Product(name='Товар C', description='Описание C', price=50.0, quantity=5)

    return [product_a, product_b, product_c]


@pytest.fixture
def test_category(test_product):
    category = Category(name='Категория 1', description='Описание категории 1')
    for product in test_product:
        category.add_product(product)

    return category
