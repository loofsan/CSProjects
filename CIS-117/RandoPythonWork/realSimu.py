import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import scipy.stats as stats


class Particle:
    """Define physics of elastic collision."""
    
    def __init__(self, mass, radius, position, velocity):
        """Initialize a Particle object
        
        mass the mass of particle
        radius the radius of particle
        position the position vector of particle
        velocity the velocity vector of particle
        """
        self.mass = mass
        self.radius = radius
        
        # last position and velocity
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        
        # all position and velocities recorded during the simulation
        self.solpos = [np.copy(self.position)]
        self.solvel = [np.copy(self.velocity)]
        self.solvel_mag = [np.linalg.norm(np.copy(self.velocity))]
        
    def compute_step(self, step):
        """Compute position of next step."""
        self.position += step * self.velocity
        self.solpos.append(np.copy(self.position)) 
        self.solvel.append(np.copy(self.velocity)) 
        self.solvel_mag.append(np.linalg.norm(np.copy(self.velocity))) 
        

    
    
    def handle_coll(self, particle):
        """Check if there is a collision with another particle."""
        
        r1, r2 = self.radius, particle.radius
        x1, x2 = self.position, particle.position
        di = x2-x1
        norm = np.linalg.norm(di)
        if norm-(r1+r2)*1.1 < 0:
            return True
        else:
            return False

    
    def resolve_coll(self, particle, step):
        """Compute velocity after collision with another particle."""
        m1, m2 = self.mass, particle.mass
        r1, r2 = self.radius, particle.radius
        v1, v2 = self.velocity, particle.velocity
        x1, x2 = self.position, particle.position
        di = x2-x1
        norm = np.linalg.norm(di)
        if norm-(r1+r2)*1.1 < step*abs(np.dot(v1-v2, di))/norm:
            self.velocity = v1 - 2. * m2/(m1+m2) * np.dot(v1-v2, di) / (np.linalg.norm(di)**2.) * di
            particle.velocity = v2 - 2. * m1/(m2+m1) * np.dot(v2-v1, (-di)) / (np.linalg.norm(di)**2.) * (-di)
            

    def compute_refl(self, step, size):
        """Compute velocity after hitting an edge.
        step the computation step
        size the medium size
        """
        r, v, x = self.radius, self.velocity, self.position
        projx = step*abs(np.dot(v,np.array([1.,0.])))
        projy = step*abs(np.dot(v,np.array([0.,1.])))
        if abs(x[0])-r < projx or abs(size-x[0])-r < projx:
            self.velocity[0] *= -1
        if abs(x[1])-r < projy or abs(size-x[1])-r < projy:
            self.velocity[1] *= -1.


def solve_step(particle_list, step, size):
    """Solve a step for every particle."""
    
    # Detect edge-hitting and collision of every particle
    for i in range(len(particle_list)):
        particle_list[i].compute_refl(step,size)
        for j in range(i+1,len(particle_list)):
                particle_list[i].resolve_coll(particle_list[j],step)    

                
    # Compute position of every particle  
    for particle in particle_list:
        particle.compute_step(step)



# Define the function for creating particles and running simulations
def init_list_random(N, radius, mass, boxsize):
    particle_list = []

    for i in range(N):
        v_mag = np.random.rand(1) * 6
        v_ang = np.random.rand(1) * 2 * np.pi
        v = np.append(v_mag * np.cos(v_ang), v_mag * np.sin(v_ang))
        
        collision = True
        while collision:
            collision = False
            pos = radius + np.random.rand(2) * (boxsize - 2 * radius)
            new_particle = Particle(mass, radius, pos, v)
            for existing_particle in particle_list:
                if new_particle.handle_coll(existing_particle):
                    collision = True
                    break
        particle_list.append(new_particle)
    return particle_list

# Define simulation parameters
particle_number = 60
boxsize = 200.0
tfin = 15
stepnumber = 70
timestep = tfin / stepnumber

# Initialize particle lists for both simulations
particles_1 = init_list_random(particle_number, radius=2, mass=1, boxsize=200)
particles_2 = init_list_random(particle_number, radius=3, mass=5, boxsize=200)

# Compute simulation steps for both sets of particles
for i in range(stepnumber):
    solve_step(particles_1, timestep, boxsize)
    solve_step(particles_2, timestep, boxsize)

# Set up subplots for four sections (two simulations, two histograms)
fig, ((ax1, hist1), (ax2, hist2)) = plt.subplots(2, 2, figsize=(12, 12))

# Set up limits and aspect ratios for the simulations
ax1.set_xlim([0, boxsize])
ax1.set_ylim([0, boxsize])
ax1.set_aspect("equal")

ax2.set_xlim([0, boxsize])
ax2.set_ylim([0, boxsize])
ax2.set_aspect("equal")

# Create circle representations for each particle in both simulations
circles_1 = [plt.Circle((p.solpos[0][0], p.solpos[0][1]), p.radius, ec="black", lw=1.5) for p in particles_1]
circles_2 = [plt.Circle((p.solpos[0][0], p.solpos[0][1]), p.radius, ec="black", lw=1.5) for p in particles_2]

# Add circles to the plots
for c in circles_1:
    ax1.add_patch(c)

for c in circles_2:
    ax2.add_patch(c)

# Function to update the plot at each frame
def update(frame):
    # Update circle positions in both simulations
    for j in range(particle_number):
        circles_1[j].center = particles_1[j].solpos[frame][0], particles_1[j].solpos[frame][1]
        circles_2[j].center = particles_2[j].solpos[frame][0], particles_2[j].solpos[frame][1]

    # Clear and replot histograms
    hist1.clear()
    hist2.clear()

    # Compute Maxwell-Boltzmann distribution for the first simulation
    k = 1.38064852e-23  # Boltzmann constant
    vel_mod_1 = [p.solvel_mag[frame] for p in particles_1]
    total_energy_1 = sum(p.mass / 2.0 * p.solvel_mag[frame] ** 2 for p in particles_1)
    average_energy_1 = total_energy_1 / len(particles_1)
    T1 = 2 * average_energy_1 / (2 * k)  # Calculate temperature-like parameter

    v1 = np.linspace(0, 12, 100)  # Speed range
    m1 = particles_1[0].mass
    f1 = m1 * np.exp(-m1 * v1 ** 2 / (2 * T1)) * 4 * np.pi * v1 ** 2  # Maxwell-Boltzmann

    # Plot histogram for the first simulation and overlay Maxwell-Boltzmann distribution
    hist1.hist(
        vel_mod_1,
        bins=12,
        density=True,
        color='skyblue',
        edgecolor='black',
        alpha=0.7,
        label="Simulation Data (R=2, M=1)",
    )

    hist1.plot(v1, f1, 'r--', linewidth=2, label="Maxwell-Boltzmann Distribution (R=2, M=1)")

    # Compute Maxwell-Boltzmann distribution for the second simulation
    vel_mod_2 = [p.solvel_mag[frame] for p in particles_2]
    total_energy_2 = sum(p.mass / 2.0 * p.solvel_mag[frame] ** 2 for p in particles_2)
    average_energy_2 = total_energy_2 / len(particles_2)
    T2 = 2 * average_energy_2 / (2 * k)  # Temperature-like parameter for the second simulation

    m2 = particles_2[0].mass
    f2 = m2 * np.exp(-m2 * v2 ** 2 / (2 * T2)) * 4 * np.pi * v2 ** 2  # Maxwell-Boltzmann

    # Plot histogram for the second simulation and overlay Maxwell-Boltzmann distribution
    hist2.hist(
        vel_mod_2,
        bins=12,
        density=True,
        color='salmon',
        edgecolor='black',
        alpha=0.7,
        label="Simulation Data (R=3, M=5)",
    )

    hist2.plot(v2, f2, 'r--', linewidth=2, label="Maxwell-Boltzmann Distribution (R=3, M=5)")

    # Set axis labels and titles
    hist1.set_xlabel("Speed")
    hist1.set_ylabel("Frequency Density")
    hist1.set_title("Particle Speed Distribution (R=2, M=1)")

    hist2.set_xlabel("Speed")
    hist2.set_ylabel("Frequency Density")
    hist2.set_title("Particle Speed Distribution (R=3, M=5)")

    # Add legends to both histograms
    hist1.legend(loc="upper right")
    hist2.legend(loc="upper right")

# Set up animation with FuncAnimation
animation = FuncAnimation(fig, update, frames=stepnumber, interval=100)

# Show the plot with animation
plt.show()