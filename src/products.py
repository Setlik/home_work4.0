class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
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
        return self.__price  # Геттер для цены

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value  # Сеттер для цены

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (f"{super().__str__()} Модель: {self.model}, Память: {self.memory} ГБ,"
                f" Цвет: {self.color}, Производительность: {self.efficiency}")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"{super().__str__()} Страна: {self.country}, "
                f"Срок прорастания: {self.germination_period} дней, Цвет: {self.color}")


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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Геттер для получения списка продуктов в виде строки."""
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __len__(self):
        return len(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"({self.name}, количество продуктов: {total_quantity} шт.)"
