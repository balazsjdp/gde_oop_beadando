from flight import Flight
from errors import INVALID_DURATION


class DomesticFlight(Flight):
    """Belföldi járatot reprezentáló osztály."""

    def __init__(self, flight_number: str, destination: str, ticket_price: float, duration_minutes: int):
        """
        Inicializálja a belföldi járatot.

        :param flight_number: A járat egyedi azonosítója.
        :param destination: A célállomás neve.
        :param ticket_price: A jegy ára forintban.
        :param duration_minutes: A repülési idő percben.
        :raises ValueError: Ha a repülési idő nem pozitív.
        """
        if duration_minutes <= 0:
            raise ValueError(INVALID_DURATION)
        super().__init__(flight_number, destination, ticket_price)
        self.__duration_minutes = duration_minutes

    @property
    def duration_minutes(self):
        """Visszaadja a repülési időt percben."""
        return self.__duration_minutes

    def flight_info(self) -> str:
        """Visszaadja a belföldi járat részletes adatait szövegként."""
        return (f"[Belföldi] {self.flight_number} | "
                f"Célállomás: {self.destination} | "
                f"Ár: {self.ticket_price} Ft | "
                f"Repülési idő: {self.__duration_minutes} perc")
