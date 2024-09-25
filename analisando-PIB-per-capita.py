import pandas as pd
import numpy as np

# lendo o csv
gdp_puro = pd.read_csv("gdp.csv")
#print(gdp_puro)           Country                                         Region      Year   GDP_pp 
#0     Afghanistan  Middle East, North Africa, and Greater Arabia  1/1/1901   613.99 
#     Afghanistan  Middle East, North Africa, and Greater Arabia  1/1/1906   624.04 
#2     Afghanistan  Middle East, North Africa, and Greater Arabia  1/1/1911   634.25
#3     Afghanistan  Middle East, North Africa, and Greater Arabia  1/1/1916   647.28
#4     Afghanistan  Middle East, North Africa, and Greater Arabia  1/1/1921   662.40
#...           ...                                            ...       ...       ...
#4414     Zimbabwe                             Sub-Saharan Africa  1/1/1991   782.09
#4415     Zimbabwe                             Sub-Saharan Africa  1/1/1996   781.50
#4416     Zimbabwe                             Sub-Saharan Africa  1/1/2001   719.96
#4417     Zimbabwe                             Sub-Saharan Africa  1/1/2006   520.17
#4418     Zimbabwe                             Sub-Saharan Africa  1/1/2011   526.33

#[4419 rows x 4 columns]


#print(gdp_puro['Year']) #O dado year está como object
#0       1/1/1901
#1       1/1/1906
#2       1/1/1911
#3       1/1/1916
#4       1/1/1921
#          ...
#4414    1/1/1991
#4415    1/1/1996
#4416    1/1/2001
#4417    1/1/2006
#4418    1/1/2011
#Name: Year, Length: 4419, dtype: object


gdp_puro['Year'] = gdp_puro['Year'].apply(lambda x: int(x.split('/')[-1]))
#print(gdp_puro['Year'])
#0       1901
#1       1906
#2       1911
#3       1916
#4       1921
#        ...
#4414    1991
#4415    1996
#4416    2001
#4417    2006
#4418    2011
#Name: Year, Length: 4419, dtype: int64

#print(gdp_puro[' GDP_pp ']) #o nome da coluna está com espaçoes antes e depois do nome
#0        613.99 
#1        624.04
#2        634.25
#3        647.28
#4        662.40
#          ...
#4414     782.09
#4415     781.50
#4416     719.96
#4417     520.17
#4418     526.33
#Name:  GDP_pp , Length: 4419, dtype: object

#print(gdp_puro[' GDP_pp '].iloc[0]) # os valore da coluna estao com espaço
# 613.99 

float(gdp_puro[' GDP_pp '].iloc[0].split()[0]) #agora goi retirado os espaços e transformando o valor em float
#613.99

gdp_puro['gdp'] = gdp_puro[' GDP_pp '].apply(lambda x: float(x.split()[0].replace(',', ''))) #removendo a virgula dos valores com virgula da coluna GDO_pp

del gdp_puro[' GDP_pp ']