from vpython import canvas, sphere, vector, rate, color
import math

# ---------- simulation parameters ----------
G = 1.0          # gravitational constant
dt = 0.0003      # smaller dt = less drift, smoother orbit
trail = True

# ---------- body class ----------
class Body:
    def __init__(self, pos, vel, mass, radius, col):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.obj = sphere(
            pos=pos,
            radius=radius,
            color=col,
            make_trail=trail,
            retain=4000   # reduced for less lag
        )

# ---------- acceleration from gravity ----------
def accel(bodies, i):
    a = vector(0, 0, 0)
    bi = bodies[i]
    for j, bj in enumerate(bodies):
        if i == j:
            continue
        r = bj.pos - bi.pos
        dist2 = r.x*r.x + r.y*r.y + r.z*r.z
        dist = dist2**0.5   # slightly faster + less rounding error
        a += G * bj.mass * r / dist**3
    return a

# ---------- scene setup ----------
scene = canvas(title="3-Body Circular Orbit",
               width=800, height=600,
               background=color.black)
scene.camera.pos = vector(0, 0, 6)
scene.camera.axis = vector(0, 0, -6)

# ---------- initial conditions ----------
R = 1.0
m = 1.0

# Slightly reduced omega for numerical stability
omega = 0.75

bodies = [
    # Body 1 (0°)
    Body(vector(R, 0, 0),
         vector(0, R*omega, 0),
         m, 0.08, color.red),

    # Body 2 (120°)
    Body(vector(R * math.cos(2*math.pi/3), R * math.sin(2*math.pi/3), 0),
         vector(-R*omega*math.sin(2*math.pi/3), R*omega*math.cos(2*math.pi/3), 0),
         m, 0.08, color.green),

    # Body 3 (240°)
    Body(vector(R * math.cos(4*math.pi/3), R * math.sin(4*math.pi/3), 0),
         vector(-R*omega*math.sin(4*math.pi/3), R*omega*math.cos(4*math.pi/3), 0),
         m, 0.08, color.blue),
]

# Precompute initial accelerations
a = [accel(bodies, i) for i in range(len(bodies))]

# ---------- main loop ----------
while True:
    rate(1200)  # smoother, less lag than 2000

    # half-step velocities
    for i, b in enumerate(bodies):
        b.vel += 0.5 * a[i] * dt

    # update positions
    for b in bodies:
        b.pos += b.vel * dt
        b.obj.pos = b.pos

    # keep camera centered on system
    com = sum((b.pos for b in bodies), vector(0,0,0)) / len(bodies)
    scene.center = com

    # new accelerations
    a_new = [accel(bodies, i) for i in range(len(bodies))]

    # finish velocity step
    for i, b in enumerate(bodies):
        b.vel += 0.5 * a_new[i] * dt

    a = a_new
