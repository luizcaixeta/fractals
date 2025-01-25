import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm  # Biblioteca para barra de progresso

def julia_set(c, xlim, ylim, resolution, max_iter=1000):
    
    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    grid = np.zeros((resolution, resolution))
    
    for i in tqdm(range(resolution), desc="Calculando conjunto de Julia"):
        for j in range(resolution):
            z = x[i] + 1j * y[j]
            iteration = 0
            while abs(z) <= 2 and iteration < max_iter:
                z = z**2 + c
                iteration += 1
            grid[j, i] = iteration
    return grid


c = complex(-0.8, 0.156)  
xlim = (-1.5, 1.5) 
ylim = (-1.5, 1.5)  
resolution = 1000  
max_iter = 500  


julia_matrix = julia_set(c, xlim, ylim, resolution, max_iter)

plt.figure(figsize=(8, 8))
plt.imshow(julia_matrix, extent=[*xlim, *ylim], cmap='inferno', origin='lower')
plt.colorbar(label='Número de iterações')
plt.title(f'Conjunto de Julia para c = {c}')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.savefig('julia_set.jpg', dpi=800)
plt.show()
