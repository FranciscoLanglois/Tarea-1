import time
import pandas as pd


#Notación: 
#values= valores de los items
#weights= volumen de los items
#capacity=capacidad máxima

       
#Se lee excel
xls = pd.ExcelFile('InstanciasKnapsack.xlsx')

#Se elige el tamaño de la instancia (S,M,L,XL)
df = pd.read_excel(xls, 'M')

#Parámetros
capacity = int(df.iloc[1, 1])

# Instancia S
#values = df.iloc[5:55, 1].values
#weights = df.iloc[5:55, 2].values

# Descomentar para instancia M
values = df.iloc[5:1005, 1].values
weights = df.iloc[5:1005, 2].values

# Descomentar para instancia L
#values = df.iloc[5:2005, 1].values
#weights = df.iloc[5:2005, 2].values

# Descomentar para instancia XL
#values = df.iloc[5:10005, 1].values
#weights = df.iloc[5:10005, 2].values


def knapsack(values, weights, capacity):
    start_time = time.time() #inicio del tiempo
    try:
        if len(values) != len(weights): #error si hay más cantidad de valores que de volumenes
            raise ValueError("Length of values and weights must be the same.")
        if capacity < 0: #error si la capacidad máxma es menor a 0
            raise ValueError("Capacity must be a non-negative integer.")
       
        n = len(values)  #número de articulos
        #crea una lista 2D para guardar el valor máximo que se puede obtener usando los primeros i articulos 
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        #construye la tabla DP de abajo hacia arriba
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                if weights[i-1] <= w:
                    #si el articulo cabe, se elige el máximo entre tomarlo y no tomarlo
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                else:
                    # si el articulo no cabe, no se lleva
                    dp[i][w] = dp[i-1][w]

        # el valor es dp[n][capacity]
        end_time = time.time() # fin del tiempo
        return {f"resultado : {dp[n][capacity]}", f" tiempo: {end_time - start_time}"}

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None 
 
result = knapsack(values, weights, capacity)
if result is not None:
    print(result)