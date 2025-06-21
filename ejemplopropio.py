import time
import pandas as pd


#Notación: 
#values= valores de los items
#weights= volumen de los items
#capacity=capacidad máxima

#def knapsack(values, weights, capacity):
    #start_time = time.time()
    #try:
        # Check for input errors
        #if len(values) != len(weights):
            #raise ValueError("Length of values and weights must be the same.")
        #if capacity < 0:
            #raise ValueError("Capacity must be a non-negative integer.")
       
        #n = len(values)  # Number of items
        # Create a 2D DP array to store the maximum value that can be obtained using the first i items and capacity
        #dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Build the DP table in bottom-up manner
        #for i in range(1, n + 1):
            #for w in range(1, capacity + 1):
                #if weights[i-1] <= w:
                    # If the current item can fit in the knapsack, choose the maximum between taking the item and not taking it
                    #dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                #else:
                    # If the current item cannot fit, do not take it
                    #dp[i][w] = dp[i-1][w]

        # The answer to the problem is in dp[n][capacity], which represents considering all items with the full capacity.
        #end_time = time.time()
        #return {f"resultado : {dp[n][capacity]}", f" tiempo: {end_time - start_time}"}

    #except ValueError as ve:
        #print(f"Input error: {ve}")
        #return None 
    #except Exception as e:
        #print(f"An unexpected error occurred: {e}")
        #return None

#Se lee excel
#xls = pd.ExcelFile('InstanciasKnapsack.xlsx')

#Se elige el tamaño de la instancia (S,M,L,XL)
#df = pd.read_excel(xls, 'S')

#Parámetros
#capacity = int(df.iloc[1, 1])

# Instancia S
#values = df.iloc[5:55, 1].values
#weights = df.iloc[5:55, 2].values

# Descomentar para instancia M
#values = df.iloc[5:1005, 1].values
#weights = df.iloc[5:1005, 2].values

# Descomentar para instancia L
#values = df.iloc[5:2005, 1].values
#weights = df.iloc[5:2005, 2].values

# Descomentar para instancia XL
#values = df.iloc[5:10005, 1].values
#weights = df.iloc[5:10005, 2].values

#result = knapsack(values, weights, capacity)
#if result is not None:
    #print(result)

##############################################################################
#Situación 1: suponga ahora que está obligado a escoger los 2 primeros objetos de cada instancia 

#Notación:
#v1=suma de volumenes de los primeros dos items
#w1=suma de valores de los primeros dos items

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
#values=df.iloc[7:1005,1].values #Volumenes
#weights=df.iloc[7:1005,2].values # Valores
#w1=970 + 760
#v1=1070 + 860

#Instancia S
#values=df.iloc[7:55,1].values
#weights=df.iloc[7:55,2].values
#w1=946 + 819
#v1=204 + 448

#capacity-=v1

#def knapsack(values, weights, capacity, w1):
    #start_time = time.time()
    #try:
        # Check for input errors
        #if len(values) != len(weights):
            #raise ValueError("Length of values and weights must be the same.")
        #if capacity < 0:
            #raise ValueError("Capacity must be a non-negative integer.")
       
        #n = len(values)  # Number of items
        # Create a 2D DP array to store the maximum value that can be obtained using the first i items and capacity
        #dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Build the DP table in bottom-up manner
        #for i in range(1, n + 1):
            #for w in range(1, capacity + 1):
                #if weights[i-1] <= w:
                    # If the current item can fit in the knapsack, choose the maximum between taking the item and not taking it
                    #dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                #else:
                    # If the current item cannot fit, do not take it
                    #dp[i][w] = dp[i-1][w]

        # The answer to the problem is in dp[n][capacity], which represents considering all items with the full capacity.
        #end_time = time.time()
        #return {f"resultado : {dp[n][capacity]+ w1}", f" tiempo: {end_time - start_time}"}

    #except ValueError as ve:
        #print(f"Input error: {ve}")
        #return None 
    #except Exception as e:
        #print(f"An unexpected error occurred: {e}")
        #return None

#result = knapsack(values, weights, capacity, w1)
#if result is not None:
    #print(result)
################################################################################
#Situación 2: considere que cada objeto tiene dos dimensiones

#Notación: 
#D=capacidad máxima de la segunada dimensión
#d=peso de los items 

xls = pd.ExcelFile('InstanciasKnapsack.xlsx')
df = pd.read_excel(xls, 'Situación 2')
#Parámetros
capacity = int(df.iloc[1, 1])
D  = int(df.iloc[2,1])

values = df.iloc[5:55, 1].values
weights = df.iloc[5:55, 2].values
d = df.iloc[5:55, 3].values

def knapsack(values, weights, d, capacity, D):
    start_time = time.time()
    try:
        #Check for input errors
        if len(values) != len(weights) or len(values) != len(d):
            raise ValueError("Length of values and weights must be the same.")
        if capacity < 0 or D < 0:
            raise ValueError("Capacity must be a non-negative integer.")
       
        n = len(values)  # Number of items
        
        dp = [[[0 for _ in range(D + 1)] for _ in range(capacity + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                for j in range(D + 1):
                    if weights[i - 1] <= w and d[i - 1] <= j:
                        dp[i][w][j] = max(dp[i - 1][w][j], dp[i - 1][w - weights[i - 1]][j - d[i - 1]] + values[i - 1])
                    else:
                        dp[i][w][j] = dp[i - 1][w][j]

        # The answer to the problem is in dp[n][capacity], which represents considering all items with the full capacity.
        end_time = time.time()
        return {f"resultado : {dp[n][capacity][D]}", f" tiempo: {end_time - start_time}"}

    except ValueError as ve:
        print(f"Input error: {ve}")
        return None 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


result = knapsack(values, weights, d, capacity, D)
if result is not None:
    print(result)