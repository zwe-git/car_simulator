import pytest
from constants import Direction
from models import CarSpec
from models.car import Car


def test_car_rotation_and_move():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands=""))
    car.rotate_left()
    assert car.direction == Direction.W
    car.rotate_right()
    assert car.direction == Direction.N


def test_car_forward_move():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.E, commands=""))
    nx, ny = car.move_forward()
    assert (nx, ny) == (1, 0)


def test_car_move_to_direction():
    car = Car(CarSpec(name="A", x=0, y=0, direction=Direction.N, commands=""))
    nx, ny = car.move_to(Direction.E)
    assert car.direction == Direction.E
    assert (nx, ny) == (1, 0)
