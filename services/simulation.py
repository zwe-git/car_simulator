from constants import Direction
from models import CarSpec
from models.car import Car

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def add_car(self, car_spec: CarSpec):
        if not self.is_inside(car_spec.x, car_spec.y):
            raise ValueError(f"Car {car_spec.name} starts outside the field at ({car_spec.x}, {car_spec.y})")
        self.cars.append(Car(car_spec))

    def is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def decide_next_position(self, car, nx, ny):
        #  Decide where the car should move next
        if self.is_inside(nx, ny):
            return (nx, ny)
        else:
            return car.current_position()

    def run(self):
        if not self.cars:
            return []
        max_steps = max(len(car.commands) for car in self.cars)
        for step in range(max_steps):
            # Each step execute car.commands[step] if available
            next_positions = {}

            for car in self.cars:
                if car.collided or step >= len(car.commands):
                    continue
                command = car.commands[step]
                if command == 'L':
                    car.rotate_left()
                elif command == 'R':
                    car.rotate_right()
                elif command == 'F':
                    nx, ny = car.move_forward()
                    next_positions[car.name] = self.decide_next_position(car, nx, ny)
                else:
                    raise ValueError(f"Invalid command: {command}")

            seen = {}
            for name, pos in next_positions.items():
                if pos in seen:
                    a = next(c for c in self.cars if c.name == name)
                    b = next(c for c in self.cars if c.name == seen[pos])
                    a.collided = True
                    b.collided = True
                else:
                    seen[pos] = name

            for car in self.cars:
                if car.collided or step >= len(car.commands):
                    continue
                if car.name in next_positions:
                    car.x, car.y = next_positions[car.name]

        return self.cars
