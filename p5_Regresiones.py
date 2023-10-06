#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.2, 3.4, 6, 8.5, 11])

# Number of data points
n = len(x)

# Calculate the coefficients
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x_squared = np.sum(x**2)
sum_xy = np.sum(x * y)

# Solve the equations A*r = b
A = np.array([[n, sum_x], [sum_x, sum_x_squared]])
b = np.array([sum_y, sum_xy])
r = np.linalg.inv(A) @ b

# Extract the coefficients of the linear regression
intercept = r[0]
slope = r[1]

# Generate points for the regression line
x_regression = np.arange(x[0], x[-1] + 0.01, 0.01)
y_regression = intercept + slope * x_regression

# Plot the data points and the regression line
plt.figure()
plt.plot(x, y, 'o', linewidth=2)
plt.grid(True)
plt.plot(x_regression, y_regression, 'r', linewidth=3)
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data Points', 'y = {} + {}x'.format(intercept, slope)], loc='best')

# Calculate the coefficient of determination (R-squared)
mean_y = np.mean(y)
SStotal = np.sum((y - mean_y)**2)
SSresidual = np.sum((y - intercept - slope * x)**2)
R2 = (SStotal - SSresidual) / SStotal
correlation = np.sqrt(R2)

# Print the equation of the line and the correlation coefficient
equation = 'y = {} + {}x'.format(intercept, slope)
print('Equation of the line: {}'.format(equation))
print('Correlation coefficient (R): {}'.format(correlation))

# Perform the regression using np.polyfit
p = np.polyfit(x, y, 1)
poly_slope = p[0]
poly_intercept = p[1]
y_poly = np.polyval(p, x_regression)

# Plot the data points and the regression line using np.polyfit
plt.figure()
plt.plot(x, y, 'o', linewidth=2)
plt.grid(True)
plt.plot(x_regression, y_poly, 'r', linewidth=3)
plt.title('Linear Regression using np.polyfit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data Points', 'y = {} + {}x'.format(poly_intercept, poly_slope)], loc='best')

plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Quadratic Regression Example
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 3.9, 7.5, 14, 21.5, 34])

n = len(x)

# Calculate the coefficients using the method of least squares
sum_xi = np.sum(x)
sum_xi2 = np.sum(x**2)
sum_xi3 = np.sum(x**3)
sum_xi4 = np.sum(x**4)
sum_yi = np.sum(y)
sum_xiyi = np.sum(x * y)
sum_xi2yi = np.sum((x**2) * y)

M = np.array([[n, sum_xi, sum_xi2],
              [sum_xi, sum_xi2, sum_xi3],
              [sum_xi2, sum_xi3, sum_xi4]])

b = np.array([sum_yi, sum_xiyi, sum_xi2yi])

coefficients = np.linalg.inv(M) @ b
a0 = coefficients[0]
a1 = coefficients[1]
a2 = coefficients[2]

x_approx = np.linspace(x[0], x[-1], 100)
y_approx = a0 + a1 * x_approx + a2 * (x_approx**2)

# Calculate the coefficient of determination (R-squared)
mean_y = np.mean(y)
St = np.sum((y - mean_y)**2)
Sr = np.sum((y - (a0 + a1 * x + a2 * (x**2)))**2)
r2 = (St - Sr) / St
r = np.sqrt(r2)

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(x, y, 'o', linewidth=3)
plt.title('Quadratic Regression (Manual)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.plot(x_approx, y_approx, 'r', linewidth=2)
plt.legend(['Data Points', f'y = {a0:.2f} + {a1:.2f}x + {a2:.2f}x^2'])

# Using the polyfit function
p = np.polyfit(x, y, 2)
ap0 = p[2]
a1 = p[1]
a2 = p[0]
x_aux = np.arange(x[0], x[-1] + 0.01, 0.01)
y_aux = np.polyval(p, x_aux)

plt.subplot(1, 2, 2)
plt.plot(x, y, 'o', linewidth=2)
plt.grid(True)
plt.plot(x_aux, y_aux, 'r', linewidth=3)
plt.title('Quadratic Regression (Polyfit)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data Points', f'y = {ap0:.2f} + {a1:.2f}x + {a2:.2f}x^2'])
plt.show()


# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# Polynomial Regression Example
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5])

# Quadratic Regression
n = len(x)
sum_xi = np.sum(x)
sum_xi2 = np.sum(x**2)
sum_xi3 = np.sum(x**3)
sum_xi4 = np.sum(x**4)
sumyi = np.sum(y)
sum_xiyi = np.sum(x * y)
sum_xi2yi = np.sum((x**2) * y)

M = np.array([[n, sum_xi, sum_xi2],
              [sum_xi, sum_xi2, sum_xi3],
              [sum_xi2, sum_xi3, sum_xi4]])

b = np.array([sumyi, sum_xiyi, sum_xi2yi])

Res = np.linalg.inv(M) @ b
a0_quad = Res[0]
a1_quad = Res[1]
a2_quad = Res[2]

x_aprox_quad = np.linspace(x[0], x[-1], 100)
y_aprox_quad = a0_quad + a1_quad * x_aprox_quad + a2_quad * (x_aprox_quad**2)

# Fourth-degree Polynomial Regression
sum_xi5 = np.sum(x**5)
sum_xi6 = np.sum(x**6)
sum_xi7 = np.sum(x**7)
sum_xi8 = np.sum(x**8)
sum_xi3yi = np.sum((x**3) * y)
sum_xi4yi = np.sum((x**4) * y)

M = np.array([[n, sum_xi, sum_xi2, sum_xi3, sum_xi4],
              [sum_xi, sum_xi2, sum_xi3, sum_xi4, sum_xi5],
              [sum_xi2, sum_xi3, sum_xi4, sum_xi5, sum_xi6],
              [sum_xi3, sum_xi4, sum_xi5, sum_xi6, sum_xi7],
              [sum_xi4, sum_xi5, sum_xi6, sum_xi7, sum_xi8]])

b = np.array([sumyi, sum_xiyi, sum_xi2yi, sum_xi3yi, sum_xi4yi])

Res = np.linalg.inv(M) @ b
a0_poly4 = Res[0]
a1_poly4 = Res[1]
a2_poly4 = Res[2]
a3_poly4 = Res[3]
a4_poly4 = Res[4]

x_aprox_poly4 = np.linspace(min(x), max(x), 100)
y_aprox_poly4 = a0_poly4 + a1_poly4 * x_aprox_poly4 + a2_poly4 * (x_aprox_poly4**2) + a3_poly4 * (x_aprox_poly4**3) + a4_poly4 * (x_aprox_poly4**4)

# Plotting the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, 'o', linewidth=3)
plt.plot(x_aprox_quad, y_aprox_quad, 'r', linewidth=2)
plt.title('Polynomial(Manual)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data Points', f'y = {a0_poly4:.2f} + {a1_poly4:.2f}x + {a2_poly4:.2f}x^2 + {a3_poly4:.2f}x^3 + {a4_poly4:.2f}x^4'], loc='upper left')
plt.grid(True)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y, 'o', linewidth=3)
plt.plot(x_aprox_poly4, y_aprox_poly4, 'r', linewidth=2)
plt.title(' Polynomial Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data Points', f'y = {a0_poly4:.2f} + {a1_poly4:.2f}x + {a2_poly4:.2f}x^2 + {a3_poly4:.2f}x^3 + {a4_poly4:.2f}x^4'], loc='upper left')
plt.grid(True)

plt.tight_layout()
plt.show()


# In[ ]:




