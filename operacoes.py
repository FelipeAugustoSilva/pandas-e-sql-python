import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())# vai imprimir:
#   col1  col2 col3
#0     1   444  abc
#1     2   555  def
#2     3   666  ghi
#3     4   444  xyz

print(df.info())# Imprime os tipos de dados da coluna
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 4 entries, 0 to 3
#Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
#---  ------  --------------  -----
# 0   col1    4 non-null      int64
# 1   col2    4 non-null      int64
# 2   col3    4 non-null      object
#dtypes: int64(2), object(1)
#memory usage: 228.0+ bytes
#None

print(df.memory_usage())# para saber qual coluna está mais pesada
#Index    132
#col1      32
#col2      32
#col3      32
#dtype: int64

print(df['col2'].unique())# vai imprimir os dados unicos da coluna 'col2'
#[444 555 666]

print(df['col2'].nunique())# vai imprimir a quantidade de valores unicos na 'col2'
#3

print(df['col2'].value_counts())# vai imprimir os valores e a quantidade de cada um
#col2
#444    2
#555    1
#666    1

def comp(x): #função
    return x ** 2 + 3
print(df['col1'].apply(comp)) #vai aplicar a função comp na col1
#0     4
#1     7
#2    12
#3    19

df['novacol'] = df['col1'].apply(comp)#Pede uma nova coluna para receber o resultado do comp sobre col1
print(df)
#   col1  col2 col3  novacol
#0     1   444  abc        4
#1     2   555  def        7
#2     3   666  ghi       12
#3     4   444  xyz       19


print(df['col1'].apply(lambda x: x ** 2 + 3))
#0     4
#1     7
#2    12
#3    19
#Name: col1, dtype: int64

print(df['col1'].sum())#somar
#10

print(df['col1'].mean())#media
#2.5

print(df['col1'].product())#multiplicação direta 
#24

print(df['col1'].std())#desvio padrao
#1.2909944487358056

print(df['col1'].max())# valor maior
#4

print(df['col1'].min())# valor menor
#1

print(df['col1'].idxmax())# id cm maior valor
#3

print(df.sort_values(by='col2'))# ordenar pela coluna
 #  col1  col2 col3  novacol
#0     1   444  abc        4
#3     4   444  xyz       19
#1     2   555  def        7
#2     3   666  ghi       12

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

dff = pd.DataFrame(data)
dict_map = {'one': '1', 'two': '2'} #determinou que quando encontar o valor ONE vai colocar o 1
dff['E'] = dff['B'].map(dict_map) #Determinou que a nova coluna 'E' vai receber o mapemaneto da coluna 'B'
print(dff)
#     A    B  C  D  E
#0  foo  one  x  1  1
#1  foo  one  y  3  1
#2  foo  two  x  2  2
#3  bar  two  y  5  2
#4  bar  one  x  4  1
#5  bar  one  y  1  1

print(dff.pivot_table(index='A', columns='B', values='D'))
#B    one  two
#A
#bar  2.5  5.0
#foo  2.0  2.0
