class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self) -> float:
        return self._price  # Геттер для цены

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value  # Сеттер для цены


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию и обновляет счетчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения списка продуктов в виде строки."""
        return "\n".join(str(product) for product in self.__products)

    def __len__(self):
        return len(self._products)
