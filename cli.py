from models.dto.car_spec import CarSpec
from services.simulation import Simulation
from constants.direction import Direction
from constants import messages

def print_welcome_screen():
    print(messages.WELCOME_MESSAGE)

def print_field_size_prompt():
    print(messages.FIELD_SIZE_PROMPT)

def print_field_created(width, height):
    print(messages.FIELD_CREATED_MESSAGE.format(width=width, height=height))

def print_main_menu():
    print("\n" + messages.CHOOSE_OPTION_MESSAGE)
    print(messages.OPTION_ADD_CAR)
    print(messages.OPTION_RUN_SIMULATION)

def print_car_name_prompt():
    print(messages.CAR_NAME_PROMPT)

def print_initial_position_prompt(name):
    print(messages.CAR_INITIAL_POSITION_PROMPT.format(name=name))

def print_commands_prompt(name):
    print(messages.CAR_COMMANDS_PROMPT.format(name=name))

def print_current_car_list(cars):
    print("\n" + messages.CURRENT_CAR_LIST)
    for car in cars:
        print(f"- {car.name}, ({car.x},{car.y}) {car.direction.value}, {''.join(car.commands)}")

def print_simulation_result(cars):
    print("\n" + messages.AFTER_SIMULATION_RESULT)
    for car in cars:
        if car.collided:
            print(f"- {car.name} collided at {car.current_position()}")
        else:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction.value}")

def print_end_menu():
    print("\n" + messages.CHOOSE_OPTION_MESSAGE)
    print(messages.OPTION_START_OVER)
    print(messages.OPTION_EXIT)

def print_goodbye_message():
    print("\n" + messages.THANK_YOU_MESSAGE)

def run():
    print_welcome_screen()
    width, height = map(int, input(messages.FIELD_SIZE_PROMPT).split())
    print_field_created(width, height)
    sim = Simulation(width, height)

    while True:
        print_main_menu()

        choice = input("> ").strip()

        if choice == '1':
            print_car_name_prompt()
            name = input().strip()
            print_initial_position_prompt(name)
            x, y, d = input().split()
            direction = Direction(d.upper())
            print_commands_prompt(name)
            commands = input().strip().upper()

            spec = CarSpec(name=name, x=int(x), y=int(y), direction=direction, commands=commands)
            sim.add_car(spec)

            print_current_car_list(sim.cars)

        elif choice == '2':
            print_current_car_list(sim.cars)

            results = sim.run()

            print_simulation_result(results)

            print_end_menu()

            next_choice = input("> ").strip()
            if next_choice == '1':
                print()
                run()
            elif next_choice == '2':
                print_goodbye_message()
                break
            else:
                print("Invalid choice, exiting.")
                break
        else:
            print("Invalid choice, please select 1 or 2.")

if __name__ == "__main__":
    run()