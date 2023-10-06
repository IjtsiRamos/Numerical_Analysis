#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Valores de los datos
x = np.array([3.0, 4.5, 7.0, 9.0])
f_x = np.array([2.5, 1.0, 2.5, 0.5])

# Longitud de los datos
n = len(x)

# Graficamos los puntos
plt.figure()
plt.subplot(211)
plt.plot(x, f_x, 'bo', linewidth=3)
plt.title('Interpolación de primer orden manual')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([x[0], x[n - 1], f_x[n - 1], f_x[0]])
plt.grid(True)

m = np.zeros(n - 1)

for k in range(n - 1):
    # Calculamos la pendiente
    m[k] = (f_x[k + 1] - f_x[k]) / (x[k + 1] - x[k])

    # Aplicamos la función lineal
    x_aux = np.linspace(x[k], x[k + 1], 100)
    f_aux = f_x[k] + m[k] * (x_aux - x[k])

    plt.plot(x_aux, f_aux, 'r', linewidth=3)

# Interpolación con función de spline
xi = np.linspace(min(x), max(x), 100)
yi = np.interp(xi, x, f_x)

plt.subplot(212)
plt.plot(x, f_x, 'o', xi, yi, '-')
plt.title('Interpolación Segmentaria Lineal en Python')
plt.xlabel('x')
plt.ylabel('f_x')

plt.tight_layout()
plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Valores obtenidos de la tabla 18.1
x = np.array([3.0, 4.5, 7.0, 9.0])
f_x = np.array([2.5, 1.0, 2.5, 0.5])

# Matriz obtenida del libro Chapra del ejemplo 18.9 datos del (18.1)
A = np.array([[4.5, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 20.25, 4.5, 1, 0, 0, 0],
              [0, 0, 49, 7, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 49, 7, 1],
              [3, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 81, 9, 1],
              [1, 0, -9, -1, 0, 0, 0, 0],
              [0, 0, 14, 1, 0, -14, -1, 0]])
r = np.array([1, 1, 2.5, 2.5, 2.5, 0.5, 0, 0])

# Determinación del vector solución
s = np.linalg.inv(A) @ r

# Calculamos los coeficientes
a1 = 0
b1 = s[0]
c1 = s[1]
a2 = s[2]
b2 = s[3]
c2 = s[4]
a3 = s[5]
b3 = s[6]
c3 = s[7]

# Graficamos los puntos de la función global
plt.figure()

# Graficamos el segmento 1
x_seg1 = np.arange(x[0], x[1], 0.01)
f_seg1 = a1 * x_seg1 ** 2 + b1 * x_seg1 + c1
plt.subplot(211)
plt.plot(x, f_x, 'bo', linewidth=3)
plt.title('Interpolación segmentaria cuadrática propia')
plt.plot(x_seg1, f_seg1, 'r', linewidth=3)

# Graficamos el segmento 2
x_seg2 = np.arange(x[1], x[2], 0.01)
f_seg2 = a2 * x_seg2 ** 2 + b2 * x_seg2 + c2
plt.plot(x_seg2, f_seg2, 'r', linewidth=3)

# Graficamos el segmento 3
x_seg3 = np.arange(x[2], x[3], 0.01)
f_seg3 = a3 * x_seg3 ** 2 + b3 * x_seg3 + c3
plt.plot(x_seg3, f_seg3, 'r', linewidth=3)

# Interpolación segmentaria cuadrática por funcion
from scipy.interpolate import interp1d
f_interp = interp1d(x, f_x, kind='quadratic')

# Puntos de evaluación
xi = np.linspace(min(x), max(x), 100)
yi = f_interp(xi)

# Graficar resultados
plt.subplot(212)
plt.plot(x, f_x, 'bo', label='Puntos')
plt.plot(xi, yi, 'r-', label='Interpolación')
plt.title('Interpolación segmentaria cuadrática python')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# In[3]:


import numpy as np

def Newtint(x, y, xx):
    # Newtint: Newton interpolating polynomial
    # yint = Newtint(x, y, xx): Uses an (n-1)-order Newton
    # interpolating polynomial based on n data points (x, y)
    # to determine a value of the dependent variable (yint)
    # at a given value of the independent variable, xx.
    # input:
    # x = independent variable
    # y = dependent variable
    # xx = value of independent variable at which
    # interpolation is calculated
    # output:
    # yint = interpolated value of dependent variable
    
    n = len(x)
    if len(y) != n:
        raise ValueError('x and y must be same length')
    
    b = np.zeros((n, n))
    b[:, 0] = y
    
    for jj in range(1, n):
        for ii in range(n - jj):
            b[ii, jj] = (b[ii+1, jj-1] - b[ii, jj-1]) / (x[ii+jj] - x[ii])
    
    xt = 1
    yint = b[0, 0]
    
    for jj in range(n - 1):
        xt *= (xx - x[jj])
        yint += b[0, jj+1] * xt
    
    return yint

def Lagrange(x, y, xx):
    # Lagrange: Lagrange interpolating polynomial
    # yint = Lagrange(x, y, xx): Uses an (n-1)-order
    # Lagrange interpolating polynomial based on n data points
    # to determine a value of the dependent variable (yint) at
    # a given value of the independent variable, xx.
    # input:
    # x = independent variable
    # y = dependent variable
    # xx = value of independent variable at which the
    # interpolation is calculated
    # output:
    # yint = interpolated value of dependent variable

    n = len(x)
    if len(y) != n:
        raise ValueError('x and y must be same length')

    s = 0
    for ii in range(n):
        product = y[ii]
        for jj in range(n):
            if ii != jj:
                product *= (xx - x[jj]) / (x[ii] - x[jj])
        s += product

    yint = s
    return yint


# In[22]:



#Se puede ingresar otro polinomio
x = [0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 3.6, 4.0, 4.4, 4.8, 5.2, 5.6, 6.0]
f_x = [1.2, 0.6, 0.3, 0.1, -0.2, -0.4, -0.5, -0.5, -0.4, -0.2, 0.1, 0.4, 0.8, 1.3]

m = len(x)
n = len(x)

xres = np.arange(x[0], x[n-1], 0.05)
xlon = len(xres)
yresNew = np.zeros(xlon)
yresLag = np.zeros(xlon)

for s in range(xlon):
    yresNew[s] = Newtint(x, f_x, xres[s])
    yresLag[s] = Lagrange(x, f_x, xres[s])

plt.figure()
plt.plot(x, f_x, 'o', linewidth=1)
plt.plot(x, f_x, 'r', linewidth=2)
plt.grid(True)
plt.plot(xres, yresNew, 'b', linewidth=6)
plt.plot(xres, yresLag, 'g', linewidth=2)
plt.show()


# In[ ]:






# In[ ]:




