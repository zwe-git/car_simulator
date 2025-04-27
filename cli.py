from models.dto.car_spec import CarSpec
from services.simulation import Simulation
from constants.direction import Direction


def run():
    print("Welcome to Auto Driving Car Simulation!")
    width, height = map(int, input("Enter width and height: ").split())
    sim = Simulation(width, height)

    while True:
        print("\n[1] Add Car\n[2] Run Simulation")
        choice = input("Choose: ").strip()

        if choice == '1':
            name = input("Car name: ").strip()
            x, y, d = input("Initial position x y Direction (N/E/S/W): ").split()
            commands = input("Commands: ").strip()
            spec = CarSpec(name=name, x=int(x), y=int(y), direction=Direction(d), commands=commands)
            sim.add_car(spec)
        elif choice == '2':
            results = sim.run()
            for car in results:
                if car.collided:
                    print(f"{car.name} collided at {car.current_position()}")
                else:
                    print(f"{car.name}: ({car.x},{car.y}) facing {car.direction.value}")
            break


if __name__ == "__main__":
    run()
