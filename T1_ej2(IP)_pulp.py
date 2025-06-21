# -*- coding: utf-8 -*-

#Se importan librerias
import time
import pulp as lp
import random
import pandas as pd

random.seed(0)  # para obtener mismo resultado siempre

#Se lee excel 
xls = pd.ExcelFile('InstanciasKnapsack.xlsx')

#Se elige el tamaño de la instancia (S,M,L,XL)
df = pd.read_excel(xls, 'M')

#Parámetros
n = int(df.iloc[0, 1])
B = int(df.iloc[1, 1])

# Instancia S
#w = df.iloc[5:55, 1].values
#v = df.iloc[5:55, 2].values

# Descomentar para instancia M
w = df.iloc[5:1005, 1].values
v = df.iloc[5:1005, 2].values

# Descomentar para instancia L
#w = df.iloc[5:2005, 1].values
#v = df.iloc[5:2005, 2].values
print(w,v)

# Descomentar para instancia XL
#w = df.iloc[5:10005, 1].values
#v = df.iloc[5:10005, 2].values

#Se comienza a medir tiempo
start_time = time.time()

#Se crea el modelo
model = lp.LpProblem("KnapsackProblem", lp.LpMaximize)

# Variables
x = lp.LpVariable.dicts('x', range(n), cat='Binary')

# Función objetivo
model += lp.lpSum([w[j] * x[j] for j in range(n)])

# Restricciones
model += lp.lpSum([v[j] * x[j] for j in range(n)]) <= B

#Se resuelve el modelo
model.solve()

#Se muestra el valor que toma cada objeto (1 si se usa, 0 si no
for j in range(n):
    print(f"x_{j+1}= {int(x[j].varValue)}")

end_time = time.time()
print(f"Tiempo Solución: {end_time - start_time} segundos")
