from dataclasses import dataclass
from constants import Direction

@dataclass
class CarSpec:
    name: str
    x: int
    y: int
    direction: Direction
    commands: str
