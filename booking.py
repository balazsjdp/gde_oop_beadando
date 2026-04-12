from datetime import datetime
from flight import Flight
from errors import EMPTY_PASSENGER_NAME, PAST_BOOKING_DATE


class Booking:
    def __init__(self, passenger_name: str, flight: Flight, date: datetime):
        """:raises ValueError: Ha az utas neve üres, vagy a dátum múltbeli."""
        self.__flight = flight
        self.passenger_name = passenger_name
        self.date = date

    @property
    def passenger_name(self):
        return self.__passenger_name

    @passenger_name.setter
    def passenger_name(self, value: str):
        if not value.strip():
            raise ValueError(EMPTY_PASSENGER_NAME)
        self.__passenger_name = value

    @property
    def flight(self):
        return self.__flight

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value: datetime):
        if value < datetime.now():
            raise ValueError(PAST_BOOKING_DATE)
        self.__date = value

    def booking_info(self) -> str:
        return (f"{self.__passenger_name} | "
                f"{self.__flight.flight_number} -> {self.__flight.destination} | "
                f"{self.__date.strftime('%Y-%m-%d')} | "
                f"Ár: {self.__flight.ticket_price} Ft")
