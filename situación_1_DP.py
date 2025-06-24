import time
import pandas as pd


#Notación: 
#values= valores de los items
#weights= volumen de los items
#capacity=capacidad máxima
#v1=suma de volumenes de los primeros dos items
#w1=suma de valores de los primeros dos items

       
#Se lee excel
xls = pd.ExcelFile('InstanciasKnapsack.xlsx')

#Se elige el tamaño de la instancia (S,M,L,XL)
df = pd.read_excel(xls, 'M')
capacity= int(df.iloc[1, 1])
#Parámetros

capacity = int(df.iloc[1, 1])

#Instancia XL
#values=df.iloc[7:10005,1].values
#weights=df.iloc[7:10005,2].values
#w1=2557 + 8974
#v1=3557 + 9974

#Instancia L
#values=df.iloc[7:2005,1].values
#weights=df.iloc[7:2005,2].values
#w1=4421 + 2085
#v1=4204 + 2448

#Instancia M
values=df.iloc[7:1005,1].values #Volumenes
weights=df.iloc[7:1005,2].values # Valores
w1=970 + 760
v1=1070 + 860

#Instancia S
#values=df.iloc[7:55,1].values
#weights=df.iloc[7:55,2].values
#w1=946 + 819
#v1=204 + 448

capacity-=v1 #se disminuye de la capacidad total el volumen de los dos primeros articulos

def knapsack(values, weights, capacity, w1):
    start_time = time.time() #inicio del tiempo
    try:
        #Check for input errors
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
        #en el resultado final se suma el valor de llevar los dos primeros articulos
        return {f"resultado : {dp[n][capacity]+ w1}", f" tiempo: {end_time - start_time}"} 

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None 
    
result = knapsack(values, weights, capacity, w1)
if result is not None:
    print(result)