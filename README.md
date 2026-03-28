# three-body-simulation
This project is a real‑time simulation that demonstrates how three planetary bodies interact under mutual gravitational attraction.   
It visualizes the classic three‑body problem using VPython and allows you to explore how different initial conditions affect the motion.

This program requires VPython for 3D graphics

## Installation

Install it with <br>
pip install vpython

Run the program as <br>
python three_body.py

## Different variable
Then a window will pop up in your browser with the animation playing


<img width="811" height="423" alt="image" src="https://github.com/user-attachments/assets/34a4cd84-9e01-42ee-86f1-83755467b89e" /> <br>
G, gravity strength (higher = faster orbits, lower = slower). <br><br>

dt, simulation time step.<br>
Smaller = smoother and more accurate.<br>
Larger = faster but less stable.<br>

pos, the body's starting position in 3D space, determines where the planet begins.<br>
vel, the initial velocity, controls the direction and speed at which the planet moves at the start.<br>
mass, how heavy the body is, higher mass means stronger gravity pull on other bodies.<br>
radius, the visual size of the sphere, only affects appearance, not physics.<br>
col, the color of the body, purely visual.<br>
make_trail, whether the body leaves a trail behind it as it moves.<br>
retain, how long the trail is, higher values mean longer trails but more lag.<br>
