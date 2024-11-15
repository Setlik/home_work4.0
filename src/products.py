from src.base_product import BaseProduct
from src.logger_mixin import CreationLoggerMixin


class Product(CreationLoggerMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    def get_product_info(self) -> str:
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Quantity: {self.quantity}"

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
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
