from datetime import datetime
from airline import Airline
from domestic_flight import DomesticFlight
from international_flight import InternationalFlight
from errors import EMPTY_PASSENGER_NAME, EMPTY_FLIGHT_NUMBER


def setup(airline: Airline):
    """Demo adatok betöltése: járatok és előre rögzített foglalások."""
    f1 = DomesticFlight("MALÉV001", "Debrecen", 8900, 45)
    f2 = DomesticFlight("MALÉV002", "Pécs", 7500, 40)
    f3 = InternationalFlight("MALÉV003", "London", 45000, "UK")

    for flight in [f1, f2, f3]:
        airline.add_flight(flight)

    pre_bookings = [
        ("It Aladár",           "MALÉV001",     datetime(2026, 6, 1)),
        ("Disz Nóra",           "MALÉV001",     datetime(2026, 6, 3)),
        ("Para Zita",           "MALÉV002",     datetime(2026, 6, 5)),
        ("Vicc Elek",           "MALÉV002",     datetime(2026, 6, 7)),
        ("Szabó László",        "MALÉV003",     datetime(2026, 6, 10)),
        ("Tejes B. Ödön",       "MALÉV003",     datetime(2026, 6, 15)),
    ]
    for name, flight_number, date in pre_bookings:
        airline.book_ticket(name, flight_number, date)


def menu():
    """Kiírja a főmenü opcióit."""
    print("\n=== Repülőjegy Foglalási Rendszer ===\n"
          "1. Jegy foglalása\n"
          "2. Foglalás lemondása\n"
          "3. Foglalások listázása\n"
          "0. Kilépés")


def get_passenger_and_flight() -> tuple | None:
    """
    Bekéri az utas nevét és a járatszámot a felhasználótól.

    :return: (utas neve, járatszám) tuple, vagy None, ha valamelyik mező üres.
    """
    passenger = input("Utas neve: ").strip()
    if not passenger:
        print(f"Hiba: {EMPTY_PASSENGER_NAME}")
        return None
    flight_number = input("Járatszám: ").strip()
    if not flight_number:
        print(f"Hiba: {EMPTY_FLIGHT_NUMBER}")
        return None
    return passenger, flight_number


def main():
    """A program belépési pontja. Elindítja a foglalási rendszert."""
    airline = Airline("****MALÉV****")
    setup(airline)

    while True:
        menu()
        choice = input("Válassz: ").strip()

        if choice == "1":
            result = get_passenger_and_flight()
            if result is None:
                continue
            passenger, flight_number = result
            date_str = input("Dátum (ÉÉÉÉ-HH-NN): ").strip()
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                price = airline.book_ticket(passenger, flight_number, date)
                print(f"Sikeres foglalás! Fizetendő: {price} Ft")
            except ValueError as e:
                print(f"Hiba: {e}")

        elif choice == "2":
            result = get_passenger_and_flight()
            if result is None:
                continue
            passenger, flight_number = result
            try:
                airline.cancel_booking(passenger, flight_number)
                print("Foglalás sikeresen lemondva.")
            except ValueError as e:
                print(f"Hiba: {e}")

        elif choice == "3":
            bookings = airline.list_bookings()
            if not bookings:
                print("Nincsenek aktuális foglalások.")
            else:
                print("\n--- Aktuális foglalások ---")
                for booking in bookings:
                    print(booking.booking_info())

        elif choice == "0":
            print("Viszlát!")
            break

        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    main()
