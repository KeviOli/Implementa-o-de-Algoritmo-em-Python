# air_reservation_system.py

class Flight:
    def __init__(self, flight_number, departure, destination, seats):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.seats = seats

class Reservation:
    def __init__(self, flight_number):
        self.flight_number = flight_number

class AirReservationSystem:
    def __init__(self):
        self.flights = {}
        self.reservations = []

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def search_flights(self, departure, destination):
        available_flights = []
        for flight_number, flight in self.flights.items():
            if flight.departure == departure and flight.destination == destination and flight.seats > 0:
                available_flights.append(flight_number)
        return available_flights

    def make_reservation(self, flight_number):
        if flight_number in self.flights and self.flights[flight_number].seats > 0:
            self.flights[flight_number].seats -= 1
            reservation = Reservation(flight_number)
            self.reservations.append(reservation)
            return True
        else:
            return False

    def view_reservations(self):
        return [reservation.flight_number for reservation in self.reservations]

    def cancel_reservation(self, flight_number):
        for reservation in self.reservations:
            if reservation.flight_number == flight_number:
                self.flights[flight_number].seats += 1
                self.reservations.remove(reservation)
                return True
        return False
