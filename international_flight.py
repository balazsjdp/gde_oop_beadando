from flight import Flight


class InternationalFlight(Flight):
    """Nemzetközi járatot reprezentáló osztály."""

    def __init__(self, flight_number: str, destination: str, ticket_price: float, country: str):
        """
        Inicializálja a nemzetközi járatot.

        :param flight_number: A járat egyedi azonosítója.
        :param destination: A célállomás neve.
        :param ticket_price: A jegy ára forintban.
        :param country: A célország neve.
        """
        super().__init__(flight_number, destination, ticket_price)
        self.__country = country

    @property
    def country(self):
        """Visszaadja a célország nevét."""
        return self.__country

    def flight_info(self) -> str:
        """Visszaadja a nemzetközi járat részletes adatait szövegként."""
        return (f"[Nemzetközi] {self.flight_number} | "
                f"Célállomás: {self.destination}, {self.__country} | "
                f"Ár: {self.ticket_price} Ft")
