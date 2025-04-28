from models.dto.car_spec import CarSpec
from services.simulation import Simulation
from constants.direction import Direction


def run():
    print("Welcome to Auto Driving Car Simulation!")
    width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
    sim = Simulation(width, height)

    while True:
        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")

        choice = input("> ").strip()

        if choice == '1':
            name = input("Please enter the name of the car: ").strip()
            x, y, d = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
            direction = Direction(d.upper())
            commands = input(f"Please enter the commands for car {name}: ").strip().upper()

            spec = CarSpec(name=name, x=int(x), y=int(y), direction=direction, commands=commands)
            sim.add_car(spec)

            print("\nYour current list of cars are:")
            for car in sim.cars:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction.value}, {''.join(car.commands)}")

        elif choice == '2':
            results = sim.run()
            print("\nAfter simulation, the result is:")
            for car in results:
                if car.collided:
                    print(f"- {car.name} collided at {car.current_position()}")
                else:
                    print(f"- {car.name}, final position: {car.current_position()} facing {car.direction.value}")

            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")

            next_choice = input("> ").strip()
            if next_choice == '1':
                print("\nRestarting simulation...\n")
                run()  # restart
            elif next_choice == '2':
                print("\nThank you for running the simulation. Goodbye!")
                break
            else:
                print("Invalid choice, exiting.")
                break
        else:
            print("Invalid choice, please select 1 or 2.")

    if __name__ == "__main__":
        run()