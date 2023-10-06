#!/usr/bin/env python
# coding: utf-8

# # Euler Method

# In[33]:


import numpy as np
import pandas as pd

def euler_method(dydx, x, step, initial_y=1):
    num_steps = len(x)
    y_euler = [initial_y] + [0] * (num_steps - 1)
    for k in range(num_steps - 1):
        f = dydx(x[k], y_euler[k])
        y_euler[k + 1] = y_euler[k] + f * step
    return y_euler

dydx = lambda x, y: 2 - np.exp(-4 * x) - 2 * y
y_x = lambda x: 1 + 0.5 * np.exp(-4 * x) - 0.5 * np.exp(-2 * x)

# Initial values
step = 0.1
x_vals = np.arange(0, 4, step)

# Exact solution table
Y_v = y_x(x_vals)
Y_E = euler_method(dydx, x_vals, step)

# Global Error
E_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    E_GE[k] = round(((Y_v[k] - Y_E[k]) / Y_v[k]) * 100, 1)

# Local Error
E_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    E_LE[k + 1] = round((((Y_v[k] - Y_E[k]) - (Y_v[k + 1] - Y_E[k + 1])) / Y_v[k + 1]) * -100, 2)

# Print the exact solution table
df_euler = pd.DataFrame({'x': x_vals, 'y_verd': Y_v, 'y_euler': Y_E,
                         'Error Global Euler': E_GE, 'Error Local Euler': E_LE})
print(df_euler)

plt.plot(x_vals, Y_v, label='True')
plt.plot(x_vals, Y_E, 'o--', label='Heun')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# In[32]:


dydx = lambda x, y: -0.5* np.exp(x/2)*np.sin(5*x)+ 5* np.exp(x/2)*np.cos(5*x)
y_x = lambda x: np.exp(x/2)*np.sin(5*x)

# Initial values
step = 0.1
x_vals = np.arange(0, 4, step)

# Exact solution table
Y_v = y_x(x_vals)
Y_E = euler_method(dydx, x_vals, step, initial_y=0)

# Global Error
E_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    E_GE[k] = round(((Y_v[k] - Y_E[k]) / Y_v[k]) * 100, 1)

# Local Error
E_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    E_LE[k + 1] = round((((Y_v[k] - Y_E[k]) - (Y_v[k + 1] - Y_E[k + 1])) / Y_v[k + 1]) * -100, 2)

# Print the exact solution table
df_euler = pd.DataFrame({'x': x_vals, 'y_verd': Y_v, 'y_euler': Y_E,
                         'Error Global Euler': E_GE, 'Error Local Euler': E_LE})
print(df_euler)

plt.plot(x_vals, Y_v, label='True')
plt.plot(x_vals, Y_E, 'o--', label='Heun')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# # Heun method

# In[169]:


import numpy as np
import pandas as pd

def heun_method_second_order(f, x, step, initial_y, initial_v):
    num_steps = len(x)
    y_heun = [initial_y] + [0] * (num_steps - 1)
    v_heun = [initial_v] + [0] * (num_steps - 1)
    for k in range(num_steps - 1):
        f1 = v_heun[k]
        f2 = f(x[k], y_heun[k], v_heun[k])
        y_predictor = y_heun[k] + f1 * step
        v_predictor = v_heun[k] + f2 * step
        f3 = f(x[k + 1], y_predictor, v_predictor)
        y_heun[k + 1] = y_heun[k] + ((f1 + f3) / 2) * step
        v_heun[k + 1] = v_heun[k] + ((f2 + f3) / 2) * step
    return y_heun

# Define the second-order ODE
dydx = lambda x, y, v: 4 * v + 3 * y - np.exp(x)
y_x = lambda x: (1/2) * np.exp(x) - (1/2) * np.exp(3 * x)

# Initial values
step = 0.05
x_vals = np.arange(0, 0.4, step)

# Solve the second-order ODE using Heun's method
Y_H = heun_method_second_order(dydx, x_vals, step, initial_y=0, initial_v=-0.03)
Y_v = y_x(x_vals)

# Global Error
H_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    H_GE[k] = round(((Y_v[k] - Y_H[k]) / Y_v[k]) * 100, 1)

# Local Error
H_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    H_LE[k + 1] = round((((Y_v[k] - Y_H[k]) - (Y_v[k + 1] - Y_H[k + 1])) / Y_v[k + 1]) * -100, 2)

# Print the exact solution table
df_heun = pd.DataFrame({'x': x_vals, 'y_verd': Y_v, 'y_heun': Y_H,
                        'Error Global Heun': H_GE, 'Error Local Heun': H_LE})
print(df_heun)

plt.plot(x_vals, Y_v, label='True')
plt.plot(x_vals, Y_H, 'o--', label='Heun')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# In[161]:


dydx = lambda x, y, v: x**2 - 2*v - y
y_x = lambda x: x*(1 - x) + 1

# Initial values
step = 0.05
x_vals = np.arange(0, 0.5, step)

# Solve the second-order ODE using Heun's method
Y_H = heun_method_second_order(dydx, x_vals, step, initial_y=1, initial_v=-3.4)

Y_v = y_x(x_vals)

# Global Error
H_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    H_GE[k] = round(((Y_v[k] - Y_H[k]) / Y_v[k]) * 100, 1)

# Local Error
H_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    H_LE[k + 1] = round((((Y_v[k] - Y_H[k]) - (Y_v[k + 1] - Y_H[k + 1])) / Y_v[k + 1]) * -100, 2)

# Print the exact solution table
df_heun = pd.DataFrame({'x': x_vals, 'y_verd': Y_v, 'y_heun': Y_H,
                        'Error Global Heun': H_GE, 'Error Local Heun': H_LE})
print(df_heun)

# Plot the true values and the calculated values
plt.plot(x_vals, Y_v, label='True')
plt.plot(x_vals, Y_H, 'o--', label='Heun')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# # Runge-Kutta method third order

# In[158]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def runge_kutta_third_order(f, x, step, initial_u, initial_v, initial_w):
    num_steps = len(x)
    u_rk = [initial_u] + [0] * (num_steps - 1)
    v_rk = [initial_v] + [0] * (num_steps - 1)
    w_rk = [initial_w] + [0] * (num_steps - 1)
    for k in range(num_steps - 1):
        u = u_rk[k]
        v = v_rk[k]
        w = w_rk[k]
        k1 = step * v
        l1 = step * w
        m1 = step * (4*u - 3*v)
        k2 = step * (v + 0.5*m1)
        l2 = step * (w + 0.5*l1)
        m2 = step * (4*(u + 0.5*k1) - 3*(v + 0.5*m1))
        k3 = step * (v + 0.5*m2)
        l3 = step * (w + 0.5*l2)
        m3 = step * (4*(u + 0.5*k2) - 3*(v + 0.5*m2))
        k4 = step * (v + m3)
        l4 = step * (w + l3)
        m4 = step * (4*(u + k3) - 3*(v + m3))
        u_rk[k + 1] = u + (k1 + 2*k2 + 2*k3 + k4) / 6
        v_rk[k + 1] = v + (l1 + 2*l2 + 2*l3 + l4) / 6
        w_rk[k + 1] = w + (m1 + 2*m2 + 2*m3 + m4) / 6
    return u_rk

# Define the third-order ODE
du3dx3 = lambda x, u, v, w: np.exp(-x)
u_x = lambda x: 2+ 2*x**2 +np.exp(x) 

# Initial values
step = 0.1
x_vals = np.arange(0, 1.1, step)

# Solve the third-order ODE using Runge-Kutta method
U_RK = runge_kutta_third_order(du3dx3, x_vals, step, initial_u=3, initial_v=1, initial_w=3.5)
U_v = u_x(x_vals)

# Global Error
RK_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    RK_GE[k] = round(((U_v[k] - U_RK[k]) / U_v[k]) * 100, 1)

# Local Error
RK_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    RK_LE[k + 1] = round((((U_v[k] - U_RK[k]) - (U_v[k + 1] - U_RK[k + 1])) / U_v[k + 1]) * -100, 2)

# Print the exact solution table
df_rk = pd.DataFrame({'x': x_vals, 'u_verd': U_v, 'u_rk': U_RK,
                      'Error Global RK': RK_GE, 'Error Local RK': RK_LE})
print(df_rk)

# Plot the true values and the calculated values
plt.plot(x_vals, U_v, label='True')
plt.plot(x_vals, U_RK, 'o--', label='Runge-Kutta')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()


# In[153]:


# Define the third-order ODE
dy3dx3 = lambda x, y, v, w: 3*np.sin(x)
y_x = lambda x: 3*np.cos(x)+ ((x**2)/2)-2

# Initial values
step = 0.1
x_vals = np.arange(0, 1.1, step)

# Solve the third-order ODE using Runge-Kutta method
Y_RK = runge_kutta_third_order(dy3dx3, x_vals, step, initial_u=1, initial_v=0, initial_w=-3.7)
Y_v = y_x(x_vals)

# Global Error
RK_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    RK_GE[k] = round(((Y_v[k] - Y_RK[k]) / Y_v[k]) * 100, 1)

# Local Error
RK_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    RK_LE[k + 1] = round((((Y_v[k] - Y_RK[k]) - (Y_v[k + 1] - Y_RK[k + 1])) / Y_v[k + 1]) * -100, 2)

# Print the exact solution table
df_rk = pd.DataFrame({'x': x_vals, 'y_verd': Y_v, 'y_rk': Y_RK,
                      'Error Global RK': RK_GE, 'Error Local RK': RK_LE})
print(df_rk)
plt.plot(x_vals, Y_v, label='True')
plt.plot(x_vals, Y_RK, 'o--', label='Runge-Kutta')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()


# # Runge-Kutta method for fourth order

# In[132]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def runge_kutta_fourth_order(f, x, step, initial_u, initial_v, initial_w, initial_z):
    num_steps = len(x)
    u_rk = [initial_u] + [0] * (num_steps - 1)
    v_rk = [initial_v] + [0] * (num_steps - 1)
    w_rk = [initial_w] + [0] * (num_steps - 1)
    z_rk = [initial_z] + [0] * (num_steps - 1)
    for k in range(num_steps - 1):
        u = u_rk[k]
        v = v_rk[k]
        w = w_rk[k]
        z = z_rk[k]
        k1 = step * v
        l1 = step * w
        m1 = step * z
        n1 = step * f(x[k], u, v, w, z)
        k2 = step * (v + 0.5*n1)
        l2 = step * (w + 0.5*m1)
        m2 = step * (z + 0.5*l1)
        n2 = step * f(x[k] + 0.5*step, u + 0.5*k1, v + 0.5*n1, w + 0.5*m1, z + 0.5*l1)
        k3 = step * (v + 0.5*n2)
        l3 = step * (w + 0.5*m2)
        m3 = step * (z + 0.5*l2)
        n3 = step * f(x[k] + 0.5*step, u + 0.5*k2, v + 0.5*n2, w + 0.5*m2, z + 0.5*l2)
        k4 = step * (v + n3)
        l4 = step * (w + m3)
        m4 = step * (z + l3)
        n4 = step * f(x[k] + step, u + k3, v + n3, w + m3, z + l3)
        u_rk[k + 1] = u + (k1 + 2*k2 + 2*k3 + k4) / 6
        v_rk[k + 1] = v + (l1 + 2*l2 + 2*l3 + l4) / 6
        w_rk[k + 1] = w + (m1 + 2*m2 + 2*m3 + m4) / 6
        z_rk[k + 1] = z + (n1 + 2*n2 + 2*n3 + n4) / 6
    return u_rk

# Define the fourth-order ODE
du_dx = lambda x, u, v, w, z: 2 * np.sin(x) - 3 * v + 4 * w - 5 * z
u_x = lambda x: np.exp(2 * x) - np.cos(x) + np.sin(x) - x

# Initial values
step = 0.1
x_vals = np.arange(0, 1.1, step)

# Solve the fourth-order ODE using Runge-Kutta method
Y_RK = runge_kutta_fourth_order(du_dx, x_vals, step, initial_u=0, initial_v=2, initial_w=7, initial_z=5)
Y_v = u_x(x_vals)

# Global Error
RK_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    RK_GE[k] = round(((Y_v[k] - Y_RK[k]) / Y_v[k]) * 100, 1)

# Local Error
RK_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    RK_LE[k + 1] = round((((Y_v[k] - Y_RK[k]) - (Y_v[k + 1] - Y_RK[k + 1])) / Y_v[k + 1]) * -100, 2)

# Print the exact solution table
df_rk = pd.DataFrame({'x': x_vals, 'u_verd': Y_v, 'u_rk': Y_RK, 'Error Global RK': RK_GE, 'Error Local RK': RK_LE})
print(df_rk)

# Plot the results
plt.plot(x_vals, Y_v, label='True')
plt.plot(x_vals, Y_RK, 'o--', label='Runge-Kutta')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()


# In[149]:


du_dx = lambda x, y, v, w, z: 6 * y - 5 * v + 4 * w - 3 * z - 2 * np.sin(x)
u_x = lambda x: np.exp(x) + x**2 - x + 1

# Initial values
step = 0.1
x_vals = np.arange(0, 1.1, step)

# Solve the fourth-order ODE using Runge-Kutta method
Y_RK = runge_kutta_fourth_order(du_dx, x_vals, step, initial_u=2, initial_v=0, initial_w=2, initial_z=3)
Y_v = u_x(x_vals)

# Global Error
RK_GE = [0] * len(x_vals)
for k in range(len(x_vals)):
    RK_GE[k] = round(((Y_v[k] - Y_RK[k]) / Y_v[k]) * 100, 1)

# Local Error
RK_LE = [0] * len(x_vals)
for k in range(len(x_vals) - 1):
    RK_LE[k + 1] = round((((Y_v[k] - Y_RK[k]) - (Y_v[k + 1] - Y_RK[k + 1])) / Y_v[k + 1]) * -100, 2)

# Print the exact solution table
df_rk = pd.DataFrame({'x': x_vals, 'u_verd': Y_v, 'u_rk': Y_RK, 'Error Global RK': RK_GE, 'Error Local RK': RK_LE})
print(df_rk)

# Plot the results
plt.plot(x_vals, Y_v, label='True')
plt.plot(x_vals, Y_RK, 'o--', label='Runge-Kutta')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




