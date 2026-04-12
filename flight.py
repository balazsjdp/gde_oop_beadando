from abc import ABC, abstractmethod
from errors import NEGATIVE_PRICE


class Flight(ABC):
    """Absztrakt alaposztály minden járattípushoz."""

    def __init__(self, flight_number: str, destination: str, ticket_price: float):
        """
        Inicializálja a járat alapadatait.

        :param flight_number: A járat egyedi azonosítója.
        :param destination: A célállomás neve.
        :param ticket_price: A jegy ára forintban.
        """
        self.__flight_number = flight_number
        self.__destination = destination
        self.__ticket_price = ticket_price

    @property
    def flight_number(self):
        """Visszaadja a járatszámot."""
        return self.__flight_number

    @property
    def destination(self):
        """Visszaadja a célállomást."""
        return self.__destination

    @property
    def ticket_price(self):
        """Visszaadja a jegy árát."""
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value: float):
        """
        Beállítja a jegy árát.

        :param value: Az új ár forintban. Nem lehet negatív.
        :raises ValueError: Ha az ár negatív.
        """
        if value < 0:
            raise ValueError(NEGATIVE_PRICE)
        self.__ticket_price = value

    @abstractmethod
    def flight_info(self) -> str:
        """Visszaadja a járat részletes adatait szövegként."""
        pass
