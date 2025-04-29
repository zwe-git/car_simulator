from cli import *
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