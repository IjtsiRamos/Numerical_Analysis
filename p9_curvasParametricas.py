#!/usr/bin/env python
# coding: utf-8

# # Curva Parametrico

# In[33]:


import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(t, points):
    n = len(points)
    result = np.zeros_like(t)
    
    for i in range(n):
        numerator = np.ones_like(t)
        denominator = np.ones_like(t)
        
        for j in range(n):
            if i != j:
                numerator *= (t - points[j][0])
                denominator *= (points[i][0] - points[j][0])
        
        result += (numerator / denominator) * points[i][1]
    
    return result

# Puntos de la curva paramétrica (coordenadas ti, xi)
points_x = [(0, -1),
            (0.25, 0),
            (0.5, 1),
            (0.75, 0),
            (1, 1)]

# Puntos de la curva paramétrica (coordenadas ti, yi)
points_y = [(0, 0),
            (0.25, 1),
            (0.5, 0.5),
            (0.75, 0),
            (1, -1)]

# Valores de t para los cuales queremos calcular los puntos de la curva
t = np.linspace(0, 1, 100)

# Calculamos las coordenadas x e y de la curva paramétrica
x = lagrange_interpolation(t, points_x)
y = lagrange_interpolation(t, points_y)

# Graficamos la curva paramétrica
plt.scatter([x[1] for x in points_x], [x[1] for x in points_y])
plt.plot(x, y)
plt.title('Curva paramétrica')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[ ]:




