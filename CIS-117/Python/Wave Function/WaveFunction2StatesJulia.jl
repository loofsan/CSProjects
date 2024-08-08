using Pkg
Pkg.add("Plots")
Pkg.add("LinearAlgebra")

using Plots
using LinearAlgebra

# Constants
L = 1.0  # Box dimension (assuming a cubic box for simplicity)
Nx, Ny, Nz = 100, 100, 100  # Number of points in each dimension

# Create grid
x = range(0, stop=L, length=Nx)
y = range(0, stop=L, length=Ny)
z = range(0, stop=L, length=Nz)
X, Y, Z = [repeat(reshape(x, :, 1, 1), 1, Ny, Nz),
           repeat(reshape(y, 1, :, 1), Nx, 1, Nz),
           repeat(reshape(z, 1, 1, :), Nx, Ny, 1)]

# Normalization constant
A = (2 / L) ^ (3 / 2)

# Wave function
function psi(nx, ny, nz, X, Y, Z)
    return A * sin.(nx * π * X / L) .* sin.(ny * π * Y / L) .* sin.(nz * π * Z / L)
end

# Ground state wave function (n_x = 1, n_y = 1, n_z = 1)
psi_111 = psi(1, 1, 1, X, Y, Z)

# First excited state wave function (n_x = 2, n_y = 1, n_z = 1)
psi_211 = psi(2, 1, 1, X, Y, Z)

# Probability densities
prob_density_111 = abs2.(psi_111)
prob_density_211 = abs2.(psi_211)

# Plotting the probability densities
plot1 = surface(x, y, prob_density_111[:, :, div(Nz, 2)], 
    title="Probability Density for Ground State (n=1,1,1)", 
    xlabel="X", ylabel="Y", zlabel="|ψ|^2", 
    legend=false, c=:viridis)

plot2 = surface(x, y, prob_density_211[:, :, div(Nz, 2)], 
    title="Probability Density for First Excited State (n=2,1,1)", 
    xlabel="X", ylabel="Y", zlabel="|ψ|^2", 
    legend=false, c=:viridis)

# Display the plots
display(plot(plot1, plot2, layout=(1, 2), size=(1200, 600)))

# Keep the plot window open until Enter is pressed
println("Press Enter to exit...")
readline()

#= For notebook
begin
	using Pkg
	Pkg.add("Plots")
	Pkg.add("LinearAlgebra")
	
	using Plots
	using LinearAlgebra
	
	# Constants
	L = 1.0  # Box dimension (assuming a cubic box for simplicity)
	Nx, Ny, Nz = 100, 100, 100  # Number of points in each dimension
	
	# Create grid
	x = range(0, stop=L, length=Nx)
	y = range(0, stop=L, length=Ny)
	z = range(0, stop=L, length=Nz)
	X, Y, Z = [repeat(reshape(x, :, 1, 1), 1, Ny, Nz),
	           repeat(reshape(y, 1, :, 1), Nx, 1, Nz),
	           repeat(reshape(z, 1, 1, :), Nx, Ny, 1)]
	
	# Normalization constant
	A = (2 / L) ^ (3 / 2)
	
	# Wave function
	function psi(nx, ny, nz, X, Y, Z)
	    return A * sin.(nx * π * X / L) .* sin.(ny * π * Y / L) .* sin.(nz * π * Z / L)
	end
	
	# Ground state wave function (n_x = 1, n_y = 1, n_z = 1)
	psi_111 = psi(1, 1, 1, X, Y, Z)
	
	# First excited state wave function (n_x = 2, n_y = 1, n_z = 1)
	psi_211 = psi(2, 1, 1, X, Y, Z)
	
	# Probability densities
	prob_density_111 = abs2.(psi_111)
	prob_density_211 = abs2.(psi_211)
	
	# Plotting the probability densities
	plot1 = surface(x, y, prob_density_111[:, :, div(Nz, 2)], 
	    title="Probability Density for Ground State (n=1,1,1)", 
	    xlabel="X", ylabel="Y", zlabel="|ψ|^2", 
	    legend=false, c=:viridis)
	
	plot2 = surface(x, y, prob_density_211[:, :, div(Nz, 2)], 
	    title="Probability Density for First Excited State (n=2,1,1)", 
	    xlabel="X", ylabel="Y", zlabel="|ψ|^2", 
	    legend=false, c=:viridis)
	
	plot(plot1, plot2, layout=(1, 2), size=(1200, 600))

end
=#