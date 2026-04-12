from flight import Flight
from errors import INVALID_DURATION


class DomesticFlight(Flight):
    def __init__(self, flight_number: str, destination: str, ticket_price: float, duration_minutes: int):
        """:raises ValueError: Ha a repülési idő nem pozitív."""
        if duration_minutes <= 0:
            raise ValueError(INVALID_DURATION)
        super().__init__(flight_number, destination, ticket_price)
        self.__duration_minutes = duration_minutes

    @property
    def duration_minutes(self):
        return self.__duration_minutes

    def flight_info(self) -> str:
        return (f"[Belföldi] {self.flight_number} | "
                f"Célállomás: {self.destination} | "
                f"Ár: {self.ticket_price} Ft | "
                f"Repülési idő: {self.__duration_minutes} perc")
