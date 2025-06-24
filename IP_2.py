

# Se importan librerías
import time
import pulp as lp
import random
import pandas as pd

random.seed(0)  # para obtener mismo resultado siempre

# Se lee Excel
xls = pd.ExcelFile('InstanciasKnapsack.xlsx')

# Se elige el tamaño de la instancia (entre 'L', 'S', 'M' y XL)
df = pd.read_excel(xls, 'L')

# Parámetros
n = int(df.iloc[0, 1])  # número de objetos
B = int(df.iloc[1, 1])  # capacidad

# Se leen exactamente n filas desde la fila 5 en adelante
w = df.iloc[5:5 + n, 1].values  # valores
v = df.iloc[5:5 + n, 2].values  # volúmenes

# Se comienza a medir tiempo
start_time = time.time()

# Se crea el modelo
model = lp.LpProblem("KnapsackProblem", lp.LpMaximize)

# Variables binarias x_j
x = lp.LpVariable.dicts('x', range(n), cat='Binary')

# Función objetivo: maximizar el valor total
model += lp.lpSum([w[j] * x[j] for j in range(n)])

# Restricción de capacidad (volumen total ≤ B)
model += lp.lpSum([v[j] * x[j] for j in range(n)]) <= B

# RESTRICCIÓN ADICIONAL: forzar que los 2 primeros objetos estén en la mochila
model += x[0] == 1
model += x[1] == 1

# Se resuelve el modelo
model.solve()

# Se mide tiempo final
end_time = time.time()

# Obtener resultados
selected_items = [j for j in range(n) if x[j].varValue == 1]
total_value = sum(w[j] for j in selected_items)
total_volume = sum(v[j] for j in selected_items)

# Mostrar resultados
print("Objetos seleccionados:", len(selected_items))
print("Valor total:", total_value)
print("Volumen total usado:", total_volume)
print("Tiempo de solución:", round(end_time - start_time, 2), "segundos")
