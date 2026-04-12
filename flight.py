from abc import ABC, abstractmethod
from errors import NEGATIVE_PRICE


class Flight(ABC):
    def __init__(self, flight_number: str, destination: str, ticket_price: float):
        self.__flight_number = flight_number
        self.__destination = destination
        self.__ticket_price = ticket_price

    @property
    def flight_number(self):
        return self.__flight_number

    @property
    def destination(self):
        return self.__destination

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value: float):
        """:raises ValueError: Ha az ár negatív."""
        if value < 0:
            raise ValueError(NEGATIVE_PRICE)
        self.__ticket_price = value

    @abstractmethod
    def flight_info(self) -> str:
        pass
