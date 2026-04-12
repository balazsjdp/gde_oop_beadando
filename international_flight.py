from flight import Flight


class InternationalFlight(Flight):
    def __init__(self, flight_number: str, destination: str, ticket_price: float, country: str):
        super().__init__(flight_number, destination, ticket_price)
        self.__country = country

    @property
    def country(self):
        return self.__country

    def flight_info(self) -> str:
        return (f"[Nemzetközi] {self.flight_number} | "
                f"Célállomás: {self.destination}, {self.__country} | "
                f"Ár: {self.ticket_price} Ft")
