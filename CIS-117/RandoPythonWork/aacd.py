import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.stats as stats

# Define the Particle class
class Particle:
    """Define physics of elastic collision."""
    
    def __init__(self, mass, radius, position, velocity):
        self.mass = mass
        self.radius = radius
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.solpos = [np.copy(self.position)]
        self.solvel = [np.copy(self.velocity)]
        self.solvel_mag = [np.linalg.norm(self.velocity)]

    def compute_step(self, step):
        """Compute position for the next step."""
        self.position += step * self.velocity
        self.solpos.append(np.copy(self.position))
        self.solvel.append(np.copy(self.velocity))
        self.solvel_mag.append(np.linalg.norm(self.velocity))
    
    def handle_coll(self, other_particle):
        """Check if there's a collision with another particle."""
        r1, r2 = self.radius, other_particle.radius
        x1, x2 = self.position, other_particle.position
        dist = np.linalg.norm(x2 - x1)
        return dist < (r1 + r2)

    def resolve_coll(self, other_particle, step):
        """Resolve collision between two particles."""
        m1, m2 = self.mass, other_particle.mass
        r1, r2 = self.radius, other_particle.radius
        v1, v2 = self.velocity, other_particle.velocity
        x1, x2 = self.position, other_particle.position
        d = x2 - x1
        dist = np.linalg.norm(d)
        
        # Check if they collide
        if dist < (r1 + r2):
            normal = d / dist
            relative_velocity = v1 - v2
            speed_along_normal = np.dot(relative_velocity, normal)
            if speed_along_normal > 0:
                return
            
            restitution = 1  # Coefficient of restitution for elastic collision
            impulse = (2 * speed_along_normal) / (m1 + m2)
            
            self.velocity -= impulse * m2 * normal
            other_particle.velocity += impulse * m1 * normal

    def compute_refl(self, step, boxsize):
        """Handle reflection off the box walls."""
        r, v, x = self.radius, self.velocity, self.position
        projx = step * abs(v[0])
        projy = step * abs(v[1])
        
        # Reflect off the box edges
        if abs(x[0]) - r < projx or abs(boxsize - x[0]) - r < projx:
            self.velocity[0] *= -1
        if abs(x[1]) - r < projy or abs(boxsize - x[1]) - r < projy:
            self.velocity[1] *= -1


# Function to solve a step for each particle
def solve_step(particle_list, step, boxsize):
    # Handle collisions with walls and between particles
    for particle in particle_list:
        particle.compute_refl(step, boxsize)
    
    # Handle particle-particle collisions
    n = len(particle_list)
    for i in range(n):
        for j in range(i + 1, n):
            if particle_list[i].handle_coll(particle_list[j]):
                particle_list[i].resolve_coll(particle_list[j], step)
    
    # Update particle positions
    for particle in particle_list:
        particle.compute_step(step)


# Function to initialize a list of random particles
def init_list_random(N, radius, mass, boxsize):
    particle_list = []
    
    for i in range(N):
        v_mag = np.random.rand(1) * 6  # Random initial velocity magnitude
        v_ang = np.random.rand(1) * 2 * np.pi  # Random direction
        v = np.array([v_mag * np.cos(v_ang), v_mag * np.sin(v_ang)]).flatten()
        
        collision = True
        while collision:
            collision = False
            pos = radius + np.random.rand(2) * (boxsize - 2 * radius)
            new_particle = Particle(mass, radius, pos, v)
            
            # Check for collisions with existing particles
            for existing_particle in particle_list:
                if new_particle.handle_coll(existing_particle):
                    collision = True
                    break
            
        particle_list.append(new_particle)
    
    return particle_list


# Constants and parameters
particle_number = 30  # Number of particles in each group
boxsize = 200.0
stepnumber = 70
timestep = 0.21

# Create two sets of particles with different radii and masses
small_particles = init_list_random(particle_number, radius=2, mass=1, boxsize=boxsize)
large_particles = init_list_random(particle_number, radius=3, mass=5, boxsize=boxsize)

# Combine the two lists for simulation
particle_list = small_particles + large_particles

# Simulate the motion of particles
for i in range(stepnumber):
    solve_step(particle_list, timestep, boxsize)

# Plotting
fig, (ax, hist) = plt.subplots(1, 2, figsize=(12, 6))

# Set the plot limits
ax.set_xlim([0, boxsize])
ax.set_ylim([0, boxsize])
ax.set_aspect("equal")

# Initialize particle representations
circles = [plt.Circle((p.solpos[0][0], p.solpos[0][1]), p.radius, ec="black", lw=1.5) for p in particle_list]
for c in circles:
    ax.add_patch(c)

# Initialize histogram data
vel_mod = [p.solvel_mag[0] for p in particle_list]

# Create the initial histogram
hist.hist(vel_mod, bins=30, density=True, label="Simulation Data")
hist.set_xlabel("Speed")
hist.set_ylabel("Frequency Density")
hist.set_title("Initial Speed Distribution")

# Function to update the animation
def update(frame):
    # Update particle positions
    for j, c in enumerate(circles):
        c.center = particle_list[j].solpos[frame][0], particle_list[j].solpos[frame][1]

    # Clear the histogram and replot
    hist.clear()
    
    # Get the velocity magnitudes at the current frame
    vel_mod = [p.solvel_mag[frame] for p in particle_list]

    # Plot the histogram
    hist.hist(
        vel_mod,
        bins=12,  # Change number of bins
        density=True,
        color='skyblue',  # Change histogram color
        edgecolor='black',  # Change edge color
        alpha=0.7,  # Adjust transparency
        label="Simulation Data",
    )
    
    # Compute Maxwell–Boltzmann distribution
    k = 1.38064852e-23
    m = 1  # Assuming a common mass for simplicity
    v = np.linspace(0, 10, 120)
    T = np.mean([p.solvel_mag[frame] ** 2 for p in particle_list]) * m / k
    mb_dist = (2 * np.pi * m / (2 * np.pi * T * k)) * np.exp(-m * v ** 2 / (2 * T * k))
    
    hist.plot(v, mb_dist, color='red', linestyle='--', label="Maxwell-Boltzmann Distribution")
    hist.legend(loc="upper right")
    hist.set_xlabel("Speed")
    hist.set_ylabel("Frequency Density")

# Set up animation with FuncAnimation
animation = FuncAnimation(fig, update, frames=stepnumber, interval=100)

# Show the plot with animation
plt.show()
