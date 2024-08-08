import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
L = 1.0  # Box dimension (assuming a cubic box for simplicity)
Nx, Ny, Nz = 100, 100, 100  # Number of points in each dimension

# Create grid
x = np.linspace(0, L, Nx)
y = np.linspace(0, L, Ny)
z = np.linspace(0, L, Nz)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# Normalization constant
A = (2 / L) ** (3 / 2)

# Wave functions
def psi(nx, ny, nz, X, Y, Z):
    return A * np.sin(nx * np.pi * X / L) * np.sin(ny * np.pi * Y / L) * np.sin(nz * np.pi * Z / L)

# Ground state wave function (n_x = 1, n_y = 1, n_z = 1)
psi_111 = psi(1, 1, 1, X, Y, Z)

# First excited state wave function (n_x = 2, n_y = 1, n_z = 1)
psi_211 = psi(2, 1, 1, X, Y, Z)

# Probability densities
prob_density_111 = np.abs(psi_111) ** 2
prob_density_211 = np.abs(psi_211) ** 2

# Plotting the probability densities
fig = plt.figure(figsize=(12, 6))

# Ground state
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X[:, :, 50], Y[:, :, 50], prob_density_111[:, :, 50], cmap='viridis')
ax1.set_title('Probability Density for Ground State (n=1,1,1)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('|ψ|^2')

# First excited state
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X[:, :, 50], Y[:, :, 50], prob_density_211[:, :, 50], cmap='viridis')
ax2.set_title('Probability Density for First Excited State (n=2,1,1)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('|ψ|^2')

plt.tight_layout()
plt.show()

