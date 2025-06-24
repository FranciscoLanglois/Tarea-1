import time
import pandas as pd


#Notación: 
#values= valores de los items
#weights= volumen de los items
#capacity=capacidad máxima
#D=capacidad máxima de la segunada dimensión
#d=peso de los items 
       
#Se lee excel
xls = pd.ExcelFile('InstanciasKnapsack.xlsx')
#Se elige la situación 2
df = pd.read_excel(xls, 'Situación 2')

#Parámetros
capacity = int(df.iloc[1, 1])
D  = int(df.iloc[2,1])

values = df.iloc[5:55, 1].values
weights = df.iloc[5:55, 2].values
d = df.iloc[5:55, 3].values

def knapsack(values, weights, d, capacity, D):
    start_time = time.time() #inicio del tiempo
    try:
        if len(values) != len(weights) or len(values) != len(d): #error si hay más cantidad de valores que de volumenes
            raise ValueError("Length of values and weights must be the same.")
        if capacity < 0 or D < 0: #error si la capacidad máxma es menor a 0
            raise ValueError("Capacity must be a non-negative integer.")
       
        n = len(values)  #número de articulos
        #crea una lista 3D para guardar el valor máximo que se puede obtener usando los primeros i articulos 
        dp = [[[0 for _ in range(D + 1)] for _ in range(capacity + 1)] for _ in range(n + 1)]
        #construye la tabla DP de abajo hacia arriba
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                for j in range(D + 1):
                    #si el articulo cabe tanto en peso como en volumen, se elige el máximo entre tomarlo y no tomarlo
                    if weights[i - 1] <= w and d[i - 1] <= j:
                        dp[i][w][j] = max(dp[i - 1][w][j], dp[i - 1][w - weights[i - 1]][j - d[i - 1]] + values[i - 1])
                    else: # si el articulo no cabe, no se lleva
                        dp[i][w][j] = dp[i - 1][w][j]

       # el valor es dp[n][capacity][D]
        end_time = time.time() # fin del tiempo
        return {f"resultado : {dp[n][capacity][D]}", f" tiempo: {end_time - start_time}"}

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None 
    
result = knapsack(values, weights, d, capacity, D)
if result is not None:
    print(result)