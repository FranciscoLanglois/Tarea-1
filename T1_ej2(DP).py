# -*- coding: utf-8 -*-
import time
import pandas as pd
import numpy as np

#Solución inspirada en 
#http://www.es.ele.tue.nl/education/5MC10/Solutions/knapsack.pdf
#y
#https://www.geeksforgeeks.org/space-optimized-dp-solution-0-1-knapsack-problem/amp/

#Notacion:
#v=volumenes de los items
#w=valores de los items
#n=numero de items
#B=Capacidad máxima de la mochila
#dp[W+1] almacena el resultado final

#Se lee excel
xls = pd.ExcelFile('InstanciasKnapsack.xlsx')

#Se elige el tamaño de la instancia (S,M,L,XL)
df = pd.read_excel(xls, 'M')

#Parámetros
n=df.iloc[0][1] #numero de items
B=df.iloc[1][1] #capacidad máxima de mochila

#Instancia XL
#w=df.iloc[5:10005,1].values
#v=df.iloc[5:10005,2].values

#Instancia L
#w=df.iloc[5:2005,1].values
#v=df.iloc[5:2005,2].values

#Instancia M
w=df.iloc[5:1005,1].values #Volumenes
v=df.iloc[5:1005,2].values # Valores

#Instancia S
#w=df.iloc[5:55,1].values
#v=df.iloc[5:55,2].values
#print(w,v)

#Se define una función que resuelve el problema de knapsack 0-1.
#A través de DP, optimizando espacio/memoria
def KnapSack(w, v, n, B): 
    seconds = time.time()       #Se comienza a medir tiempo
    dp = np.zeros(B+1)          #Se crea array para almacenar el resultado final. 
                                #dp[i] almacena el valor del knapsack para capacidad "i"
    keep = np.zeros((n+1,B+1))  #Se crea una variable que guarda las decisiones 1-0 tomadas
    sol=np.zeros(n)
    for i in range(n):          #Se itera sobre todos los items 
        for j in range(B,v[i]-1,-1): 
                                    #Se recorre el array de derecha a izquierda
                                     #desde B a v[i]-1 (busca hasta v[i] inclusive)
                                     #es decir, se parte con la mochila vacía
            print(dp)
            if dp[j]>w[i] + dp[j-v[i]]:
                keep[i,j]=0     #Se guarda la decisión de no poner el item i en la mochila
            else:
                keep[i,j]=1     #Se guarda la decisión de poner el item i en la mochila
            dp[j] = max(dp[j] , w[i] + dp[j-v[i]]); #Recursion
        
            #La recursión consiste en encontrar el máximo entre dp[j] y 
            #w[i] + dp[j-v[i]] 
    K=B    
    #Para guardar las decisiones tomadas 0-1 con respecto a los items
    for i in range(n,0,-1): 
        if keep[i-1,K]==1:
            K=K-v[i-1]
            sol[i-1]=1

    #Se termina de medir el tiempo
    seconds2 = time.time()
    return dp[B],seconds2-seconds,sol

fo,time,sol=KnapSack(w, v, n, B) #valor funcion objetivo, tiempo, solucion
print(fo,time,sol)