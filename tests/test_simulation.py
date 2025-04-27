import pytest
from constants import Direction
from models import CarSpec
from services import Simulation


def test_single_car_simulation():
    sim = Simulation(10, 10)
    sim.add_car(CarSpec(name="A", x=1, y=2, direction=Direction.N, commands="FFRFFFFRRL"))
    results = sim.run()

    car = next(c for c in results if c.name == "A")
    assert (car.x, car.y) == (5, 4)  # Correct final position after executing all commands
    assert car.direction == Direction.S  # Correct final direction
    assert not car.collided  # Should not collide


def test_multiple_car_collision():
    sim = Simulation(10, 10)
    sim.add_car(CarSpec(name="A", x=1, y=2, direction=Direction.N, commands="FFRFFFFRRL"))
    sim.add_car(CarSpec(name="B", x=7, y=8, direction=Direction.W, commands="FFLFFFFFFF"))
    results = sim.run()

    car_a = next(c for c in results if c.name == "A")
    car_b = next(c for c in results if c.name == "B")

    # Both should have collided
    assert car_a.collided
    assert car_b.collided

    # They should have collided at the same position
    assert car_a.current_position() == (4, 4)
    assert car_b.current_position() == (5, 5)
