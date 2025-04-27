from constants import Direction
from models import CarSpec
from models.car import Car


class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def add_car(self, car_spec: CarSpec):
        self.cars.append(Car(car_spec))

    def is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def run(self):
        print(f"Starting simulation with {len(self.cars)} cars.")
        for car in self.cars:
            print(f"- Car {car.name} starts at {car.current_position()} facing {car.direction}")

        max_steps = max(len(car.commands) for car in self.cars)
        for step in range(max_steps):
            # Each step execute car.commands[step] if available
            print(f"\n=== Step {step + 1} ===")
            next_positions = {}

            for car in self.cars:
                if car.collided or step >= len(car.commands):
                    continue

                command = car.commands[step]
                print(f"Car {car.name} command: {command}")

                if command == 'L':
                    car.rotate_left()
                    print(f" -> Car {car.name} rotated left, now facing {car.direction}")
                elif command == 'R':
                    car.rotate_right()
                    print(f" -> Car {car.name} rotated right, now facing {car.direction}")
                elif command == 'F':
                    nx, ny = car.move_forward()
                    if self.is_inside(nx, ny):
                        next_positions[car.name] = (nx, ny)
                        print(f" -> Car {car.name} moves forward to ({nx},{ny})")
                    else:
                        next_positions[car.name] = car.current_position()
                        print(f" -> Car {car.name} tried to move outside field. Staying at {car.current_position()}")
                elif command in ('N', 'E', 'S', 'W'):
                    nx, ny = car.move_to(Direction(command))
                    if self.is_inside(nx, ny):
                        next_positions[car.name] = (nx, ny)
                        print(f" -> Car {car.name} rotates to face {Direction(command)} and moves to ({nx},{ny})")
                    else:
                        next_positions[car.name] = car.current_position()
                        print(
                            f" -> Car {car.name} tried to move outside field after rotating. Staying at {car.current_position()}")
                else:
                    raise ValueError(f"Invalid command: {command}")

            # Detect collisions
            seen = {}
            for name, pos in next_positions.items():
                if pos in seen:
                    a = next(c for c in self.cars if c.name == name)
                    b = next(c for c in self.cars if c.name == seen[pos])
                    a.collided = True
                    b.collided = True
                    print(f"!!! Collision detected between Car {a.name} and Car {b.name} at {pos}")
                else:
                    seen[pos] = name

            # Update positions for cars that have not collided
            for car in self.cars:
                if car.collided or step >= len(car.commands):
                    continue
                if car.name in next_positions:
                    car.x, car.y = next_positions[car.name]

        print("\n=== Simulation finished ===")
        for car in self.cars:
            if car.collided:
                print(f"Car {car.name} collided at {car.current_position()}")
            else:
                print(f"Car {car.name} final position: {car.current_position()}, facing {car.direction}")

        return self.cars
