from datetime import datetime
from flight import Flight
from errors import EMPTY_PASSENGER_NAME, PAST_BOOKING_DATE


class Booking:
    """Egy jegyfoglalást reprezentáló osztály."""

    def __init__(self, passenger_name: str, flight: Flight, date: datetime):
        """
        Inicializálja a foglalást.

        :param passenger_name: Az utas neve.
        :param flight: A foglalt járat.
        :param date: A repülés dátuma.
        :raises ValueError: Ha az utas neve üres, vagy a dátum múltbeli.
        """
        self.__flight = flight
        self.passenger_name = passenger_name
        self.date = date

    @property
    def passenger_name(self):
        """Visszaadja az utas nevét."""
        return self.__passenger_name

    @passenger_name.setter
    def passenger_name(self, value: str):
        """
        Beállítja az utas nevét.

        :param value: Az utas neve. Nem lehet üres.
        :raises ValueError: Ha a név üres.
        """
        if not value.strip():
            raise ValueError(EMPTY_PASSENGER_NAME)
        self.__passenger_name = value

    @property
    def flight(self):
        """Visszaadja a foglalt járatot."""
        return self.__flight

    @property
    def date(self):
        """Visszaadja a foglalás dátumát."""
        return self.__date

    @date.setter
    def date(self, value: datetime):
        """
        Beállítja a foglalás dátumát.

        :param value: A repülés dátuma. Nem lehet múltbeli.
        :raises ValueError: Ha a dátum múltbeli.
        """
        if value < datetime.now():
            raise ValueError(PAST_BOOKING_DATE)
        self.__date = value

    def booking_info(self) -> str:
        """Visszaadja a foglalás részletes adatait szövegként."""
        return (f"{self.__passenger_name} | "
                f"{self.__flight.flight_number} -> {self.__flight.destination} | "
                f"{self.__date.strftime('%Y-%m-%d')} | "
                f"Ár: {self.__flight.ticket_price} Ft")
