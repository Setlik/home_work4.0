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
