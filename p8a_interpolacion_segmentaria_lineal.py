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
