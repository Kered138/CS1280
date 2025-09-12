import numpy as np 
import matplotlib.pyplot as plt 

G = 1.0
dt = 0.01
steps = 5000

class Body:
    def __init__(self, mass, x,y, vx = 0, vy = 0):
        self.mass = mass
        self.pos = np.array([x,y], dtype = float)
        self.vel = np.array([vx,vy], dtype = float)
def compute_force(b1 ,b2):
    diff = b2.pos - b1.pos
    r = np.linalg.norm(diff)
    if r == 0: return np.array([0.0,0.0])
    force_mag = G * b1.mass * b2.mass / r**2
    return force_mag * diff / r
bodies = [
    Body(1000,0,0),
    Body(1,5,0, vy=8.0)
]
trajectories = [[] for _ in bodies]
for _ in range(steps):
    forces = [np.array([0.0,0.0]) for _ in bodies]

    for i in range(len(bodies)):
        for j in range(i +1, len(bodies)):
            f = compute_force(bodies[i], bodies[j])
            forces[i] += f
            forces[j] += f
    for i, body in enumerate(bodies):
        acc = forces[i] / body.mass
        body.vel += acc * dt
        body.pos += body.vel * dt
        trajectories[i].append(body.pos.copy())

for traj in trajectories:
    traj = np.array(traj)
    plt.plot(traj[:,0], traj[:,1])
plt.gca().set_aspect('equal')
plt.show()