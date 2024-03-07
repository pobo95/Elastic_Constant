import numpy as np
from math import sqrt, acos, degrees

def read_POSCAR(filename):
    with open(filename, 'r') as f:
        # Skip the comment line
        comment_line = f.readline()
        # Read scaling factor
        scaling_factor = float(f.readline().strip())
        # Read lattice vectors
        lattice_vectors = []
        for _ in range(3):
            line = f.readline().split()
            lattice_vectors.append([float(x) for x in line])
    return scaling_factor, lattice_vectors

def calculate_parameters(scaling_factor, lattice_vectors):
    # Scale lattice vectors
    scaled_lattice_vectors = np.array(lattice_vectors) * scaling_factor

    # Extract components
    A = np.array(scaled_lattice_vectors[0])
    B = np.array(scaled_lattice_vectors[1])
    C = np.array(scaled_lattice_vectors[2])

    # Calculate lengths
    a = np.linalg.norm(A)
    b = np.linalg.norm(B)
    c = np.linalg.norm(C)

    # Calculate angles in radians
    alpha = acos(np.dot(B, C) / (b * c))
    beta = acos(np.dot(A, C) / (a * c))
    gamma = acos(np.dot(A, B) / (a * b))

    # Convert angles to degrees
    alpha_deg = degrees(alpha)
    beta_deg = degrees(beta)
    gamma_deg = degrees(gamma)

    # Calculate volume
    v = np.dot(A, np.cross(B, C))

    return a, b, c, alpha_deg, beta_deg, gamma_deg, v

# Example usage
filename = "POSCAR"
scaling_factor, lattice_vectors = read_POSCAR(filename)
a, b, c, alpha, beta, gamma, volume = calculate_parameters(scaling_factor, lattice_vectors)

# Output results
print("a =", a)
print("b =", b)
print("c =", c)
print("alpha =", alpha)
print("beta =", beta)
print("gamma =", gamma)
print("Volume =", volume)
