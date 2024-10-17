from src.products import Category, Product


def test_product_initialization(sample_product):
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_category_initialization(sample_category):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == ("Смартфоны, как средство не только коммуникации, "
                                           "но и получения дополнительных функций для удобства жизни")
    assert len(sample_category.products) == 1
    assert sample_category.products[0].name == "Samsung Galaxy S23 Ultra"


def test_category_count_increment(sample_category):
    initial_count = Category.category_count
    Category(name="Another Category", description="Another description.", products=[])
    assert Category.category_count == initial_count + 1


def test_product_count_increment(sample_category):
    initial_count = Category.product_count
    Category(name="Another Category", description="Another description.",
             products=[Product("New Product", "New Description", 5.99, 10)])
    assert Category.product_count == initial_count + 1
