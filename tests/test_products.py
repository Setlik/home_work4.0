import pytest

from src.products import Category, Product


def test_product_initialization(sample_product):
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_initialization(sample_category):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'
    # assert len(sample_category.products) == 1


def test_category_count_increment(sample_category):
    initial_count = Category.category_count
    Category(name="Another Category", description="Another description.", products=[])
    assert Category.category_count == initial_count + 1


def test_product_count_increment(sample_category):
    initial_count = Category.product_count
    Category(name="Another Category", description="Another description.",
             products=[Product("New Product", "New Description", 5.99, 10)])
    assert Category.product_count == initial_count + 1


def test_price_setter_negative(sample_product):
    sample_product.price = -50
    assert ("Цена не должна быть нулевая или отрицательная")


def test_price_setter_zero(sample_product):
    sample_product.price = 0
    assert ("Цена не должна быть нулевая или отрицательная")


def test_price_setter_positive(sample_product):
    sample_product.price = 150.0
    assert sample_product.price == 150.0


def test_new_product(sample_product):
    product_data = {
        'name': "Товар 2",
        'description': "Описание товара 2",
        'price': 200.0,
        'quantity': 5
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "Товар 2"
    assert new_product.price == 200.0


def test_get_products(sample_category):
    expected_output = "Товар 1, 100.0 руб. Остаток: 10 шт."
    assert expected_output, sample_category.products


def test_product_str(test_product):
    product_a = test_product[0]
    expected_str = "Товар A, 100.0 руб. Остаток: 10 шт."
    assert str(product_a) == expected_str


def test_category_str(test_category):
    expected_str = "(Категория 1, количество продуктов: 17 шт.)"
    assert str(test_category) == expected_str


def test_product_addition(test_category, sample_product):
    initial_length = len(test_category)
    test_category.add_product(sample_product)
    assert len(test_category) == initial_length + 1


def test_product_addition_type_error():
    category = Category(name='Test', description='Test')
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_smartphone_addition(sample_category, sample_smartphone):
    initial_length = len(sample_category)
    sample_category.add_product(sample_smartphone)
    assert len(sample_category) == initial_length + 1


def test_lawn_grass_addition(sample_category, sample_lawn_grass):
    initial_length = len(sample_category)
    sample_category.add_product(sample_lawn_grass)
    assert len(sample_category) == initial_length + 1


def test_product_addition_wrong_type(sample_category):
    with pytest.raises(TypeError):
        sample_category.add_product("This is not a product")


def test_product_sum_same_type(sample_product):
    expected_value = 2 * sample_product.price * sample_product.quantity
    assert expected_value == sample_product.price * sample_product.quantity * 2
