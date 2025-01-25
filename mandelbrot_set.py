import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm 
def mandelbrot_set(xlim, ylim, resolution, max_iter=1000):

    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    mandelbrot_matrix = np.zeros((resolution, resolution))
    
    for i in tqdm(range(resolution), desc="Calculando conjunto de Mandelbrot"):
        for j in range(resolution):
            c = x[i] + 1j * y[j]
            z = 0
            iteration = 0
            while abs(z) <= 2 and iteration < max_iter:
                z = z**2 + c
                iteration += 1
            mandelbrot_matrix[j, i] = iteration
    return mandelbrot_matrix


xlim = (-2.0, 1.0)  
ylim = (-1.5, 1.5)  
resolution = 1000  
max_iter = 500  
mandelbrot_matrix = mandelbrot_set(xlim, ylim, resolution, max_iter)

plt.figure(figsize=(8, 8))
plt.imshow(mandelbrot_matrix, extent=[*xlim, *ylim], cmap='magma', origin='lower')
plt.colorbar(label='Número de iterações')
plt.title('Conjunto de Mandelbrot')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.savefig('mandelbrot_set.jpg', dpi=800)
plt.show()
