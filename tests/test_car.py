from cli import *
from constants import Direction
from models import CarSpec
from models.car import Car
from constants import messages

# Messages Tests
def simulate_cli(mocker, user_inputs):
    mocker.patch("builtins.input", side_effect=user_inputs)
    return run

def test_cli_welcome_message(capsys, mocker):
    simulate_cli(mocker, ["10 10", "2", "2"])()
    captured = capsys.readouterr()
    assert messages.WELCOME_MESSAGE in captured.out

def test_cli_field_created_message(capsys, mocker):
    simulate_cli(mocker, ["10 10", "2", "2"])()
    captured = capsys.readouterr()
    expected_message = messages.FIELD_CREATED_MESSAGE.format(width=10, height=10)
    assert expected_message in captured.out

def test_cli_add_car_prompt(capsys, mocker):
    simulate_cli(mocker, ["10 10", "1", "A", "1 2 N", "FFRFFFFRRL", "2", "2"])()
    captured = capsys.readouterr()
    assert messages.CAR_NAME_PROMPT in captured.out

def test_cli_initial_position_prompt(capsys, mocker):
    simulate_cli(mocker, ["10 10", "1", "A", "1 2 N", "FFRFFFFRRL", "2", "2"])()
    captured = capsys.readouterr()
    expected_prompt = messages.CAR_INITIAL_POSITION_PROMPT.format(name="A")
    assert expected_prompt in captured.out

def test_cli_commands_prompt(capsys, mocker):
    simulate_cli(mocker, ["10 10", "1", "A", "1 2 N", "FFRFFFFRRL", "2", "2"])()
    captured = capsys.readouterr()
    expected_prompt = messages.CAR_COMMANDS_PROMPT.format(name="A")
    assert expected_prompt in captured.out

def test_cli_after_simulation_message(capsys, mocker):
    simulate_cli(mocker, ["10 10", "2", "2"])()
    captured = capsys.readouterr()
    assert messages.AFTER_SIMULATION_RESULT in captured.out

def test_cli_goodbye_message(capsys, mocker):
    simulate_cli(mocker, ["10 10", "2", "2"])()
    captured = capsys.readouterr()
    assert messages.THANK_YOU_MESSAGE in captured.out

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