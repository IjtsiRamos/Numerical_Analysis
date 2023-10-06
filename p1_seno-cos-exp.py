#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
import matplotlib.pyplot as plt

# Numero de terminos de la serie
n=16
#Valor al cual se quiere aproximar la funcion de seno
x=0.78539816339
# Valor verdadero
Vv=math.cos(x)
#Vv=0.0137073546;
# 1a Aproximacion
cos_x=(x**0)/math.factorial(0)
# Aproximacion del valor del termino de la serie
Va=cos_x
Aact=cos_x
Aant=0
# Error verdadero (Et)-> t = true
Et=abs(((Vv-Va)/Vv)*100)
# Error aproximado (Ea)->  = approximate
Ea=abs(((Aact-Aant)/Aact)*100)
Es=(0.5)*(10**(2-n))
m=2
Ea_array=[]
Ea_array.append(Ea)
Et_array=[]
Et_array.append(Et)
while Ea>Es:
    Aant=Va
    cos_x=cos_x-(x**m)/(math.factorial(m))
    Va=cos_x
    Aact=cos_x
    Et=abs((Vv-Va)/Vv)*100
    Et_array.append(Et)
    Ea=abs((Aact-Aant)/Aact)*100
    Ea_array.append(Ea)
    m+=2
    Aant=Va
    Aant=Va
    cos_x=cos_x+(x**m)/(math.factorial(m))
    Va=cos_x
    Aact=cos_x
    Et=abs((Vv-Va)/Vv)*100
    Et_array.append(Et)
    Ea=abs((Aact-Aant)/Aact)*100
    Ea_array.append(Ea)
    m+=2   

plt.plot(Ea_array)
plt.plot(Et_array)
plt.ylabel('Porcentaje del error')
plt.xlabel('Numero de terminos de la serie')
plt.title('Grafica del error')
plt.grid(True)
plt.show()
 
print(cos_x)
print(Vv)


# In[6]:


import math
import matplotlib.pyplot as plt

# Numero de terminos de la serie
n=16
#Valor al cual se quiere aproximar la funcion de seno
x=0.78539816339
# Valor verdadero
Vv=math.sin(x)
#Vv=0.0137073546;
# 1a Aproximacion
sin_x=x
# Aproximacion del valor del termino de la serie
Va=sin_x
Aact=sin_x
Aant=0
# Error verdadero (Et)-> t = true
Et=abs(((Vv-Va)/Vv)*100)
# Error aproximado (Ea)->  = approximate
Ea=abs(((Aact-Aant)/Aact)*100)
Es=(0.5)*(10**(2-n))
m=3
Ea_array=[]
Ea_array.append(Ea)
Et_array=[]
Et_array.append(Et)
while Ea>Es:
    Aant=Va
    sin_x=sin_x-(x**m)/(math.factorial(m))
    Va=sin_x
    Aact=sin_x
    Et=abs((Vv-Va)/Vv)*100
    Et_array.append(Et)
    Ea=abs((Aact-Aant)/Aact)*100
    Ea_array.append(Ea)
    m+=2
    Aant=Va
    Aant=Va
    sin_x=sin_x+(x**m)/(math.factorial(m))
    Va=sin_x
    Aact=sin_x
    Et=abs((Vv-Va)/Vv)*100
    Et_array.append(Et)
    Ea=abs((Aact-Aant)/Aact)*100
    Ea_array.append(Ea)
    m+=2   

plt.plot(Ea_array)
plt.plot(Et_array)
plt.ylabel('Porcentaje del error')
plt.xlabel('Numero de terminos de la serie')
plt.title('Grafica del error')
plt.grid(True)
plt.show()
 
print(sin_x)
print(Vv)


# In[1]:


import math
import matplotlib.pyplot as plt

# Número de términos de la serie
n = 16
# Valor al cual se quiere aproximar la función exponencial
x = 1.0
# Valor verdadero
Vv = math.exp(x)
# 1ª Aproximación
exp_x = (x**0) / math.factorial(0)
# Aproximación del valor del término de la serie
Va = exp_x
Aact = exp_x
Aant = 0
# Error verdadero (Et) -> t = true
Et = abs(((Vv - Va) / Vv) * 100)
# Error aproximado (Ea) -> a = approximate
Ea = abs(((Aact - Aant) / Aact) * 100)
Es = (0.5) * (10**(2 - n))
m = 1
Ea_array = []
Ea_array.append(Ea)
Et_array = []
Et_array.append(Et)

while Ea > Es:
    Aant = Va
    exp_x = exp_x + (x**m) / (math.factorial(m))
    Va = exp_x
    Aact = exp_x
    Et = abs((Vv - Va) / Vv) * 100
    Et_array.append(Et)
    Ea = abs((Aact - Aant) / Aact) * 100
    Ea_array.append(Ea)
    m += 1

plt.plot(Ea_array)
plt.plot(Et_array)
plt.ylabel('Porcentaje del error')
plt.xlabel('Número de términos de la serie')
plt.title('Gráfica del error')
plt.grid(True)
plt.show()

print(exp_x)
print(Vv)


# In[ ]:




