# Driving Car Simulation

This project simulates multiple autonomous cars navigating a rectangular field. Cars can rotate, move forward, or reorient to a specific direction. The simulation detects collisions and restricts movement within field boundaries.

---

## Features

- Create a simulation field of any size.
- Add multiple cars with:
  - Unique names
  - Initial positions and directions
  - Custom movement commands
- Supported Commands:
  - `F`: Move forward
  - `L`: Rotate left (90° counterclockwise)
  - `R`: Rotate right (90° clockwise)
  - `N`, `S`, `E`, `W`: Rotate to a specific direction and move forward
- Step-by-step simulation with collision detection.
- Command-line interface (CLI) interaction.

---

## Known Limitations

- **Input Validation**:  
  The current CLI assumes that users will follow the input format instructions carefully.  
  Inputs like non-integer field sizes, invalid directions (only 'N', 'E', 'S', 'W' allowed), or invalid commands are **not explicitly validated**.  
  This decision was made intentionally to keep the simulation flow lightweight and focused on core movement logic for this assignment.

- **Synchronous Movement**:  
  Cars move one command at a time per step. Real-world asynchronous behavior (different car speeds) is not handled yet.

- **No Persistence**:  
  Field state and car states are not saved after a simulation run (no save/load feature).

---

## Future Improvements

- **Robust Input Validation**:  
  Add strong input validation for:
  - Field dimensions (must be positive integers)
  - Car initial position and direction (only 'N', 'S', 'E', 'W' accepted)
  - Command sequence (only 'F', 'L', 'R', 'N', 'S', 'E', 'W')
  - Handle unexpected user inputs gracefully with friendly error messages.

- **Advanced Movement Behavior**:  
  Support variable speeds, scheduled moves, or asynchronous simulation steps.

---

## Getting Started

```bash
git clone https://github.com/zwe-git/car_simulator.git
cd car_simulator
```
## Running the Simulator

- Run through CLI 

```bash
python -m cli
```

- Running Test

```bash
pytest -v
```