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


#print(gdp_puro.groupby('Country')['Year'].min())
#Country
#Afghanistan    1901
#Albania        1901
#Algeria        1901
#Andorra        1901
#Angola         1901
#               ... 
#Venezuela      1901
#Vietnam        1901
#Yemen, Rep.    1901
#Zambia         1901
#Zimbabwe       1901
#Name: Year, Length: 193, dtype: int64


#print(gdp_puro.groupby('Country')['Year'].min().value_counts())
#Year
#1901    192
#1991      1
#Name: count, dtype: int64


#print(gdp_puro.groupby('Country')['Year'].min()[gdp_puro.groupby('Country')['Year'].min() == 1991])
#Country
#Kosovo    1991
#Name: Year, dtype: int64


#print(gdp_puro[gdp_puro['Year'] < 2000].max())
#Country              Zimbabwe
#Region     Sub-Saharan Africa
#Year                     1996
#gdp                  118681.3

df_gdp_start = gdp_puro[gdp_puro['Year'] == 1901]
df_gdp_end = gdp_puro[gdp_puro['Year'] == 1996]

#print((df_gdp_end.groupby('Region')['gdp'].mean() / df_gdp_start.groupby('Region')['gdp'].mean() - 1) * 100)
#Region
#Asia                                             711.761516
#Australia and Oceania                            396.075383
#Central America and the Caribbean                406.426789
#Europe                                           594.046167
#Middle East, North Africa, and Greater Arabia    857.215950
#North America                                    589.760175
#South America                                    312.123735
#Sub-Saharan Africa                               248.633780
#Name: gdp, dtype: float64

#print(((df_gdp_end.groupby('Region')['gdp'].mean() / df_gdp_start.groupby('Region')['gdp'].mean() - 1) * 100).sort_values())
#Region
#Sub-Saharan Africa                               248.633780
#South America                                    312.123735
#Australia and Oceania                            396.075383
#Central America and the Caribbean                406.426789
#North America                                    589.760175
#Europe                                           594.046167
#Asia                                             711.761516
#Middle East, North Africa, and Greater Arabia    857.215950
#Name: gdp, dtype: float64