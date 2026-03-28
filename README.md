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

**pos** <br>
the body's starting position in 3D space, determines where the planet begins.<br><br>

**vel** <br>
The initial velocity controls the direction and speed at which the planet moves at the start.<br><br>

**mass** <br>
how heavy the body is, higher mass means stronger gravity pull on other bodies.<br><br>

**radius**<br>
The visual size of the sphere only affects appearance, not physics.<br><br>

**col**<br>
The color of the body is purely visual.<br><br>

**make_trail**<br>
Whether the body leaves a trail behind it as it moves.<br><br>

**retain**<br>
how long the trail is, higher values mean longer trails but more lag.<br><br>

##Camera
<img width="459" height="129" alt="image" src="https://github.com/user-attachments/assets/37346093-30eb-4772-b3cf-27c9fe513aeb" /><br>
Title: The window title. <br>
Width, height: The VPython window size. <br>
Scene.camera.pos: The position of the camera. <br>
Scene.camera.axis: The direction of the camera is pointing. <br>



