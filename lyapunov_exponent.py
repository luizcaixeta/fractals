import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from tqdm import tqdm  

sequence = 'ABABAB'

@njit
def logistic_map(x, r):
    return r * x * (1 - x)

@njit
def calculate_lyapunov(a, b, sequence, iterations=1000):
    x = 0.123
    lyapunov_exponent = 0
    S_len = len(sequence)
    
    for n in range(iterations):
        r_n = a if sequence[n % S_len] == 'A' else b
        x = logistic_map(x, r_n)
        
        value = abs(r_n * (1 - 2 * x))
        if value <= 1e-10:
            value = 1e-10
        lyapunov_exponent += np.log(value)

    lyapunov_exponent /= iterations
    return lyapunov_exponent

def calculate_lyapunov_matrix(a_vals, b_vals, sequence):
    resolution = len(a_vals)
    lyapunov_matrix = np.zeros((resolution, resolution))
    # Itera com uma barra de progresso
    for i in tqdm(range(resolution), desc="Calculando matriz de Lyapunov"):
        a = a_vals[i]
        for j in range(resolution):
            b = b_vals[j]
            lyapunov_matrix[i, j] = calculate_lyapunov(a, b, sequence)
    return lyapunov_matrix

resolution = 1000
a_vals = np.linspace(0.1, 4.0, resolution)
b_vals = np.linspace(0.1, 4.0, resolution)

lyapunov_matrix = calculate_lyapunov_matrix(a_vals, b_vals, sequence)

lambda_max = np.max(lyapunov_matrix)
lambda_min = np.min(lyapunov_matrix)

cmap_choice = 'Blues_r' if lambda_max < 0 else 'twilight'

plt.imshow(lyapunov_matrix, extent=[3.5, 4.0, 2.8, 3.4], cmap=cmap_choice, origin='lower')
plt.colorbar(label='Exponente de Lyapunov')
plt.xlabel('a')
plt.ylabel('b')
plt.title('Fractal de Lyapunov')
plt.savefig('lyapunov_exponent.jpg', dpi=800)

