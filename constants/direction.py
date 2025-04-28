from enum import Enum

class Direction(Enum):
    # Four cardinal direction to support left/right rotation logic
    N = 'N'
    W = 'W'
    S = 'S'
    E = 'E'

    def left(self):
        # Return the direction to the left (counter-clockwise)
        return {
            Direction.N: Direction.W,
            Direction.W: Direction.S,
            Direction.S: Direction.E,
            Direction.E: Direction.N,
        }[self]

    def right(self):
        # Return the direction to the right (clockwise)
        return {
            Direction.N: Direction.E,
            Direction.E: Direction.S,
            Direction.S: Direction.W,
            Direction.W: Direction.N,
        }[self]
