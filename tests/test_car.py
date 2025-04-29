import pytest
from constants import Direction
from models import CarSpec
from models.car import Car
from services import Simulation

# Rotation Tests
def test_car_rotate_left_from_north():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands=""))
    car.rotate_left()
    assert car.direction == Direction.W

def test_car_rotate_left_from_west():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.W, commands=""))
    car.rotate_left()
    assert car.direction == Direction.S

def test_car_rotate_right_from_north():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands=""))
    car.rotate_right()
    assert car.direction == Direction.E

def test_car_rotate_right_from_west():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.W, commands=""))
    car.rotate_right()
    assert car.direction == Direction.N

# Forward Movement Tests
def test_car_move_forward_north():
    car = Car(CarSpec(name="A", x=1, y=1, direction=Direction.N, commands=""))
    nx, ny = car.move_forward()
    assert (nx, ny) == (1, 2)

def test_car_move_forward_east():
    car = Car(CarSpec(name="A", x=1, y=1, direction=Direction.E, commands=""))
    nx, ny = car.move_forward()
    assert (nx, ny) == (2, 1)

def test_car_move_forward_south():
    car = Car(CarSpec(name="A", x=1, y=1, direction=Direction.S, commands=""))
    nx, ny = car.move_forward()
    assert (nx, ny) == (1, 0)

def test_car_move_forward_west():
    car = Car(CarSpec(name="A", x=1, y=1, direction=Direction.W, commands=""))
    nx, ny = car.move_forward()
    assert (nx, ny) == (0, 1)

# Move To Direction Tests
def test_car_move_to_same_direction_no_rotation():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands=""))
    car.move_to(Direction.N)
    assert car.direction == Direction.N

def test_car_move_to_different_direction_rotate_right():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands=""))
    car.move_to(Direction.E)
    assert car.direction == Direction.E

def test_car_move_to_different_direction_rotate_full_cycle():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands=""))
    car.move_to(Direction.S)
    assert car.direction == Direction.S

# Unhappy Cases
def test_add_car_outside_field_raises():
    sim = Simulation(5, 5)
    with pytest.raises(ValueError, match="starts outside the field"): sim.add_car(CarSpec(name="O", x=10, y=10, direction=Direction.N, commands="F"))

def test_car_hits_boundary_each_step():
    sim = Simulation(5, 5)
    sim.add_car(CarSpec(name="B", x=0, y=0, direction=Direction.S, commands="FFFFF"))
    result = sim.run()

    car = next(c for c in result if c.name == "B")
    assert car.current_position() == (0, 0)  # never moved

def test_cars_with_different_length_commands():
    sim = Simulation(5, 5)
    sim.add_car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands="F"))
    sim.add_car(CarSpec(name="B", x=1, y=0, direction=Direction.N, commands="FFFF"))

    result = sim.run()

    car_a = next(c for c in result if c.name == "A")
    car_b = next(c for c in result if c.name == "B")

    assert car_a.current_position() == (0, 1)
    assert car_b.current_position() == (1, 4)