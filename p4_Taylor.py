#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math

# Definición de las funciones
def func1(x):
    return math.log(x)

def func2(x):
    return math.sin(x)

# Número de términos para la serie de Taylor
N = 10

# Rango de x
x = [i * 0.01 for i in range(1, 629)]  # Rango de 0.01 a 2 * pi con incremento de 0.01

# Cálculo de la serie de Taylor y el error para la función ln(x)
taylor1 = [0.0] * len(x)
for n in range(1, N + 1):
    taylor1 = [taylor1[i] + ((-1) ** (n + 1)) * ((xi - 1) ** n) / n for i, xi in enumerate(x)]
exact1 = [func1(xi) for xi in x]
error1 = [abs(exact1[i] - taylor1[i]) for i in range(len(x))]

# Cálculo de la serie de Taylor y el error para la función seno
taylor2 = [0.0] * len(x)
for n in range(N + 1):
    taylor2 = [taylor2[i] + ((-1) ** n) * func2((2 * n + 1) * xi) / math.factorial(2 * n + 1) for i, xi in enumerate(x)]
exact2 = [func2(xi) for xi in x]
error2 = [abs(exact2[i] - taylor2[i]) for i in range(len(x))]

# Creación de la tabla
table = zip(x, exact1, taylor1, error1, exact2, taylor2, error2)
headers = [
    'x',
    'ln(x) (Exact)',
    'ln(x) (Approximation)',
    'Error',
    'sin(x) (Exact)',
    'sin(x) (Approximation)',
    'Error'
]
print('{:^10s}{:^20s}{:^25s}{:^15s}{:^20s}{:^25s}{:^15s}'.format(*headers))
for row in table:
    print('{:^10.2f}{:^20.6f}{:^25.6f}{:^15.6f}{:^20.6f}{:^25.6f}{:^15.6f}'.format(*row))


# Dibujar las funciones y sus errores
plt.figure()

plt.subplot(2, 2, 1)
plt.plot(x, [func1(xi) for xi in x], x, taylor1)
plt.title('Función exponencial y aproximación')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 2)
plt.plot(x, error1)
plt.title('Error en la aproximación de la función exponencial')
plt.xlabel('x')
plt.ylabel('Error')

plt.subplot(2, 2, 3)
plt.plot(x, [func2(xi) for xi in x], x, taylor2)
plt.title('Función seno y su aproximación')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 4)
plt.plot(x, error2)
plt.title('Error en la aproximación de la función seno')
plt.xlabel('x')
plt.ylabel('Error')

plt.tight_layout()
plt.show()


# In[ ]:




