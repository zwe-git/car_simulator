from constants import Direction
from models.dto import CarSpec


class Car:
    # Car class with position, direction, and command list  to support simulation
    def __init__(self, spec: CarSpec):
        self.name = spec.name
        self.x = spec.x
        self.y = spec.y
        self.direction = spec.direction
        self.commands = list(spec.commands)
        self.collided = False

    def current_position(self):
        return self.x, self.y

    def rotate_left(self):
        self.direction = self.direction.left()

    def rotate_right(self):
        self.direction = self.direction.right()

    def move_forward(self):
        move_map = {
            Direction.N: (0, 1),
            Direction.E: (1, 0),
            Direction.S: (0, -1),
            Direction.W: (-1, 0)
        }
        dx, dy = move_map[self.direction]
        return self.x + dx, self.y + dy

    def move_to(self, target_direction: Direction):
        while self.direction != target_direction:
            self.rotate_right()
        return self.move_forward()
