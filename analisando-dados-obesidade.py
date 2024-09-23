#importando as bibliotecas
import pandas as pd
import numpy as np

# lendo o csv
df_obesidy = pd.read_csv("obesity_cleaned.csv")
#print(df_obesidy)
#       Unnamed: 0      Country  Year       Obesity (%)         Sex
#0               0  Afghanistan  1975     0.5 [0.2-1.1]  Both sexes
#1               1  Afghanistan  1975     0.2 [0.0-0.6]        Male
#2               2  Afghanistan  1975     0.8 [0.2-2.0]      Female
#3               3  Afghanistan  1976     0.5 [0.2-1.1]  Both sexes
#4               4  Afghanistan  1976     0.2 [0.0-0.7]        Male
#...           ...          ...   ...               ...         ...
#24565       24565     Zimbabwe  2015     4.5 [2.4-7.6]        Male
#24566       24566     Zimbabwe  2015  24.8 [18.9-31.3]      Female
#24567       24567     Zimbabwe  2016  15.5 [12.0-19.2]  Both sexes
#24568       24568     Zimbabwe  2016     4.7 [2.5-8.0]        Male
#24569       24569     Zimbabwe  2016  25.3 [19.1-32.0]      Female

#[24570 rows x 5 columns]

del df_obesidy['Unnamed: 0'] # Deletando a coluna 'Unnamed: 0'
#print(df_obesidy)
#           Country  Year       Obesity (%)         Sex
#0      Afghanistan  1975     0.5 [0.2-1.1]  Both sexes
#1      Afghanistan  1975     0.2 [0.0-0.6]        Male
#2      Afghanistan  1975     0.8 [0.2-2.0]      Female
#3      Afghanistan  1976     0.5 [0.2-1.1]  Both sexes
#4      Afghanistan  1976     0.2 [0.0-0.7]        Male
#...            ...   ...               ...         ...
#24565     Zimbabwe  2015     4.5 [2.4-7.6]        Male
#24566     Zimbabwe  2015  24.8 [18.9-31.3]      Female
#24567     Zimbabwe  2016  15.5 [12.0-19.2]  Both sexes
#24568     Zimbabwe  2016     4.7 [2.5-8.0]        Male
#24569     Zimbabwe  2016  25.3 [19.1-32.0]      Female

df_obesidy['Obesity'] = df_obesidy['Obesity (%)'].apply(lambda x: x.split()[0]) # Criando a coluna Obesity que vai receber o valor do Obesity (%), vou aplicar um split para receber apenas o valor [0 da coluna]
#print(df_obesidy)
#           Country  Year       Obesity (%)         Sex Obesity
#0      Afghanistan  1975     0.5 [0.2-1.1]  Both sexes     0.5
#1      Afghanistan  1975     0.2 [0.0-0.6]        Male     0.2
#2      Afghanistan  1975     0.8 [0.2-2.0]      Female     0.8
#3      Afghanistan  1976     0.5 [0.2-1.1]  Both sexes     0.5
#4      Afghanistan  1976     0.2 [0.0-0.7]        Male     0.2

#print(df_obesidy["Obesity"].value_counts()) #precisa deletar o valor de  "No      504"
#Obesity
#No      504
#0.4     222
#0.6     218
#0.5     217
#0.7     210
#       ...
#56.8      1
#62.4      1
#60.0      1
#62.6      1
#60.3      1
#Name: count, Length: 602, dtype: int64

df_obesidy.loc[df_obesidy["Obesity"] == "No", "Obesity"] = np.nan #Estou retornando True para os valores de 'No' na coluna 'Obesity', e alterando de No para NaN
df_obesidy["Obesity"] = df_obesidy["Obesity"].dropna() #Estou dropando os valores em NaN
#print(df_obesidy["Obesity"].value_counts())
#Obesity
#.4     222
#0.6     218
#0.5     217
#0.7     210
#0.8     201
#       ...
#61.9      1
#56.8      1
#62.1      1
#42.7      1
#46.5      1
#Name: count, Length: 601, dtype: int64

df_obesidy["Obesity"] = df_obesidy["Obesity"].apply(lambda x: float(x)) # tranformando os valores da coluna Obesity em float
df_obesidy["Year"] = df_obesidy["Year"].apply(lambda x: int(x)) # transformando so valores da coluna Year em int

df_obesidy.set_index("Year", inplace=True) # tranformando os valores da coluna Year em indice e aplicando um inplace para validar

#print(df_obesidy)
#          Country       Obesity (%)         Sex  Obesity
#Year
#1975  Afghanistan     0.5 [0.2-1.1]  Both sexes      0.5
#1975  Afghanistan     0.2 [0.0-0.6]        Male      0.2
#1975  Afghanistan     0.8 [0.2-2.0]      Female      0.8
#1976  Afghanistan     0.5 [0.2-1.1]  Both sexes      0.5
#1976  Afghanistan     0.2 [0.0-0.7]        Male      0.2
#...           ...               ...         ...      ...
#2015     Zimbabwe     4.5 [2.4-7.6]        Male      4.5
#2015     Zimbabwe  24.8 [18.9-31.3]      Female     24.8
#2016     Zimbabwe  15.5 [12.0-19.2]  Both sexes     15.5
#2016     Zimbabwe     4.7 [2.5-8.0]        Male      4.7
#2016     Zimbabwe  25.3 [19.1-32.0]      Female     25.3


#df_obesidy['Sex'] = df_obesidy["Sex"].apply(lambda x: str(x))

#print(df_obesidy[df_obesidy.index == 2015].groupby("Sex").mean())

mean_values = df_obesidy[df_obesidy.index == 2015].groupby("Sex").mean(numeric_only=True)
print(mean_values)




