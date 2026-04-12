from datetime import datetime
from flight import Flight
from booking import Booking
from errors import FLIGHT_NOT_FOUND, PAST_BOOKING_DATE, DUPLICATE_BOOKING, BOOKING_NOT_FOUND


class Airline:
    def __init__(self, name: str):
        self.__name = name
        self.__flights: list[Flight] = []
        self.__bookings: list[Booking] = []

    @property
    def name(self):
        return self.__name

    def add_flight(self, flight: Flight):
        self.__flights.append(flight)

    def book_ticket(self, passenger_name: str, flight_number: str, date: datetime) -> float:
        """
        Jegyet foglal a megadott járatra.

        :param passenger_name: Az utas neve.
        :param flight_number: A foglalni kívánt járat azonosítója.
        :param date: A repülés dátuma.
        :return: A jegy ára forintban.
        :raises ValueError: Ha a járat nem létezik, a dátum múltbeli,
                            vagy az utas már foglalt erre a járatra.
        """
        flight = next((f for f in self.__flights if f.flight_number == flight_number), None)
        if flight is None:
            raise ValueError(FLIGHT_NOT_FOUND.format(flight_number))

        if date < datetime.now():
            raise ValueError(PAST_BOOKING_DATE)

        if any(b.passenger_name == passenger_name and b.flight.flight_number == flight_number
               for b in self.__bookings):
            raise ValueError(DUPLICATE_BOOKING.format(passenger_name, flight_number))

        self.__bookings.append(Booking(passenger_name, flight, date))
        return flight.ticket_price

    def cancel_booking(self, passenger_name: str, flight_number: str):
        """
        Lemondja a megadott utas foglalását az adott járaton.

        :param passenger_name: Az utas neve.
        :param flight_number: A járat azonosítója.
        :raises ValueError: Ha nem található ilyen foglalás.
        """
        booking = next(
            (b for b in self.__bookings
             if b.passenger_name == passenger_name and b.flight.flight_number == flight_number),
            None
        )
        if booking is None:
            raise ValueError(BOOKING_NOT_FOUND)
        self.__bookings.remove(booking)

    def list_bookings(self) -> list:
        return list(self.__bookings)
