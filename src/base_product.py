from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._BaseProduct__price = price
        self.quantity = quantity

    @abstractmethod
    def get_product_info(self) -> str:
        pass

    @property
    def price(self) -> float:
        return self._BaseProduct__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._BaseProduct__price = value
