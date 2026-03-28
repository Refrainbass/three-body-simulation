# Three-body-simulation
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

## Camera

<img width="459" height="129" alt="image" src="https://github.com/user-attachments/assets/37346093-30eb-4772-b3cf-27c9fe513aeb" /><br>
Title: The window title. <br>
Width, height: The VPython window size. <br>
Scene.camera.pos: The position of the camera. <br>
Scene.camera.axis: The direction of the camera is pointing. <br>

## Customizing the Bodies

<img width="783" height="123" alt="image" src="https://github.com/user-attachments/assets/0d7c70e2-3326-468b-95e3-decfb353308a" /> <br>
The first one is position; changing this will move the body to a new starting location. <br>
The second one is Velocity, changing this will change the direction and speed at which the body starts moving. <br>
The third value is Mass, changing this will change the gravity of the body; the higher the number, the stronger the pull.<br>
The fourth value is the radius, which only changes the **VISUAL** size of the body.<br>

## Math
The math used in this simulation is Newton's Law of Universal Gravitation in vector form to compute the gravitational acceleration between bodies.
<img width="644" height="356" alt="image" src="https://github.com/user-attachments/assets/bfc3b79a-7082-45ba-a48e-9c908bc49524" /> <br>
This only gives the strength of the force but not the direction, so we will need to convert it into vector form. <br>
<img width="1024" height="768" alt="image" src="https://github.com/user-attachments/assets/3b05415d-cd34-48b8-8d9b-2405aee121b4" /> <br>
Since the simulation uses acceleration instead of force:<br>
The equation will change from <br>
<img width="178" height="68" alt="image" src="https://github.com/user-attachments/assets/97b7eb8e-5ffe-4cf0-8e6f-0bd3b81ba65d" /><br>
To<br>
<img width="217" height="80" alt="image" src="https://github.com/user-attachments/assets/9f5b29bd-c3c7-440b-92ee-da53f2a4af3a" /><br>
This form includes the direction and inverse-square strength, which can be seen in the code.
<img width="365" height="23" alt="image" src="https://github.com/user-attachments/assets/a149b19a-6380-4ec0-afe8-6e85d52037c6" /><br>
It is dist**3 because r/ |r| gives the direction and 1 / |r|^z gives the strength. Combining these 2 we will get
<img width="185" height="89" alt="image" src="https://github.com/user-attachments/assets/d2c5aa4e-6d51-4138-942a-29e38e7a308f" /> <br>
Gravity will become infinite when 2 bodies get extremely close, since the simulation cannot handle that. We will add a tiny number to the equation <img width="204" height="60" alt="image" src="https://github.com/user-attachments/assets/142e54e7-5d16-42bc-b80f-c865f09a1a5e" />, which prevents infinite acceleration, and it is a standard technique in N-body simulations.<br>
This is only 1 of the many periodic solutions. More can be simulated by changing the custom bodies' values.<br>
<img width="261" height="259" alt="image" src="https://github.com/user-attachments/assets/70b75833-664b-438b-936c-873288e4c6dd" />














