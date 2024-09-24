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



mean_values = df_obesidy[df_obesidy.index == 2015].groupby("Sex").mean(numeric_only=True)
#print(mean_values)
#              Obesity
#Sex
#Both sexes  19.508377
#Female      22.899476
#Male        15.980628




df_obesidy_start = df_obesidy[df_obesidy.index == 1975]
df_obesidy_end = df_obesidy[df_obesidy.index == 2016]
df_obesidy_start.set_index('Country', inplace=True)
df_obesidy_end.set_index('Country', inplace=True)

df_obesidy_ev = df_obesidy_end[df_obesidy_end['Sex'] == 'Both sexes']['Obesity'] - df_obesidy_start[df_obesidy_start['Sex'] == 'Both sexes']['Obesity']
#print(df_obesidy_ev)
#Country
#Afghanistan                            5.0
#Albania                               15.2
#Algeria                               20.5
#Andorra                               12.7
#Angola                                 7.4
#                                      ...
#Venezuela (Bolivarian Republic of)    16.0
#Viet Nam                               2.0
#Yemen                                 14.3
#Zambia                                 6.6
#Zimbabwe                              11.8
#Name: Obesity, Length: 195, dtype: float64

#print(df_obesidy_ev.sort_values().dropna())
#Country
#Viet Nam         2.0
#Singapore        3.1
#Japan            3.3
#Bangladesh       3.4
#Timor-Leste      3.6
#                ...
#Cook Islands    27.9
#Tonga           28.3
#Kiribati        30.1
#Niue            31.1
#Tuvalu          33.7
#Name: Obesity, Length: 191, dtype: float64


#print(df_obesidy_ev.sort_values().head(5))
#Country
#Viet Nam       2.0
#Singapore      3.1
#Japan          3.3
#Bangladesh     3.4
#Timor-Leste    3.6
#Name: Obesity, dtype: float64


#print(df_obesidy_ev.sort_values().dropna().tail(5))
#Country
#Cook Islands    27.9
#Tonga           28.3
#Kiribati        30.1
#Niue            31.1
#Tuvalu          33.7
#Name: Obesity, dtype: float64


df_2015 = df_obesidy[df_obesidy.index == 2015]
#print(df_2015[df_2015['Obesity'] == df_2015['Obesity'].max()])
#     Country       Obesity (%)     Sex  Obesity
#Year
#2015   Nauru  63.1 [55.5-70.3]  Female     63.1


df_brazil = df_obesidy[df_obesidy['Country'] == 'Brazil']
#print(df_brazil[df_brazil['Sex'] == 'Female']['Obesity'] - df_brazil[df_brazil['Sex'] == 'Male']['Obesity'])
#Year
#1975    4.3
#1976    4.4
#1977    4.6
#1978    4.7
#1979    4.9
#1980    4.9
#1981    5.1
#1982    5.2
#1983    5.4
#1984    5.5
#1985    5.6
#1986    5.7
#1987    5.8
#1988    5.9
#1989    6.0
#1990    6.1
#1991    6.1
#1992    6.3
#1993    6.3
#1994    6.4
#1995    6.4
#1996    6.5
#1997    6.6
#1998    6.7
#1999    6.8
#2000    6.8
#2001    6.8
#2002    6.8
#2003    6.9
#2004    6.9
#2005    6.9
#2006    6.9
#2007    7.0
#2008    6.9
#2009    7.0
#2010    7.0
#2011    6.9
#2012    6.9
#2013    6.9
#2014    6.9
#2015    6.9
#2016    6.9
#Name: Obesity, dtype: float64




difference = df_brazil[df_brazil['Sex'] == 'Female']['Obesity'] - df_brazil[df_brazil['Sex'] == 'Male']['Obesity']
difference.plot() # Gera um grafico no notebook




df_both = df_obesidy[df_obesidy['Sex'] == 'Both sexes']
df_final = df_both.groupby('Year')['Obesity'].mean()
df_final.plot() #Gera um grafico no notebook