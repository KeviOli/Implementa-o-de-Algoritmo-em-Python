# test_air_reservation_system.py
import pytest
from air_reservation_system import Flight, Reservation, AirReservationSystem

def test_make_reservation():
    system = AirReservationSystem()
    flight = Flight("AA101", "NYC", "LA", 100)
    system.add_flight(flight)
    
    assert system.make_reservation("AA101") == True
    assert len(system.reservations) == 1
    assert system.flights["AA101"].seats == 99

def test_cancel_reservation():
    system = AirReservationSystem()
    flight = Flight("AA101", "NYC", "LA", 100)
    system.add_flight(flight)
    system.make_reservation("AA101")
    
    assert system.cancel_reservation("AA101") == True
    assert len(system.reservations) == 0
    assert system.flights["AA101"].seats == 100

def test_search_flights():
    system = AirReservationSystem()
    flight1 = Flight("AA101", "NYC", "LA", 100)
    flight2 = Flight("AA102", "LA", "NYC", 80)
    system.add_flight(flight1)
    system.add_flight(flight2)
    
    assert system.search_flights("NYC", "LA") == ["AA101"]
    assert system.search_flights("LA", "NYC") == ["AA102"]

if __name__ == "__main__":
    pytest.main(["-v", "--color=yes"])
