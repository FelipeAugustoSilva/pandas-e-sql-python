import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']

minha_lista = [10,20,30]

arr = np.array([10,20,30])

d = {'a':10, 'b':20, 'c':30}

pd.Series(labels)
print(pd.Series(labels)) # Vai imprimir:
#0    a
#1    b
#2    c
#dtype: object

pd.Series(data=labels, index=minha_lista)
print(pd.Series(data=labels, index=minha_lista))# Vai imprimir:
#10    a    // o indice da lista passou a ser os valores do minha_lista
#20    b
#30    c
#dtype: object

pd.Series(d)
print(pd.Series(d))# Vai imprimir:
#a    10
#b    20
#c    30
#dtype: int64

ser1 = pd.Series([1,2,3,4],index = ['EUA', 'Alemanha', 'USSR', 'Japão'])
print(ser1)# Vai imprimir:
#EUA         1
#Alemanha    2
#USSR        3
#Japão       4
#dtype: int64

ser2 = pd.Series([1,2,5,4],index = ['EUA', 'Alemanha', 'Italia', 'Japão'])
print(ser2)# Vai imprimir:
#EUA         1
#Alemanha    2
#Italia      5
#Japão       4
#dtype: int64

print(ser1['Japão'])# Vai imprimir:
#4

print(ser1[['Alemanha', 'Japão']])# Vai imprimir:
#Alemanha    2
#Japão       4

print(ser1 + ser2)# Vai imprimir:
#Alemanha    4.0
#EUA         2.0
#Italia      NaN
#Japão       8.0
#USSR        NaN
#dtype: float64