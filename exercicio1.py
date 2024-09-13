import pandas as pd


# Concatenando dois dataframes
df1 = pd.read_csv("gasolina_2000+.csv", index_col=0) #Estou lendo o csv e dizendo que o index é a coluna 0
df2 = pd.read_csv("gasolina_2010+.csv", index_col=0) #Estou lendo o csv e dizendo que o index é a coluna 0

df = pd.concat([df1, df2]) # concatenando o df1 com df2
#print(df.shape) # imprime o numero de linhas e colunas (120823, 18)




# Verificando o tipo de dados
#print(df.tail) e print(df.head)  # Nos ajuda a entender o tipo de dados na tabela

#print(df.info()) #vai imprimir
#<class 'pandas.core.frame.DataFrame'>
#Index: 120823 entries, 0 to 120822
#Data columns (total 18 columns):
 #   Column                         Non-Null Count   Dtype
#---  ------                         --------------   -----
# 0   DATA INICIAL                   120823 non-null  object
# 1   DATA FINAL                     120823 non-null  object
# 2   REGIÃO                         120823 non-null  object
# 3   ESTADO                         120823 non-null  object
# 4   PRODUTO                        120823 non-null  object
# 5   NÚMERO DE POSTOS PESQUISADOS   120823 non-null  int64
# 6   UNIDADE DE MEDIDA              120823 non-null  object
# 7   PREÇO MÉDIO REVENDA            120823 non-null  float64
# 8   DESVIO PADRÃO REVENDA          120823 non-null  float64
# 9   PREÇO MÍNIMO REVENDA           120823 non-null  float64
# 10  PREÇO MÁXIMO REVENDA           120823 non-null  float64
# 11  MARGEM MÉDIA REVENDA           120823 non-null  object
# 12  COEF DE VARIAÇÃO REVENDA       120823 non-null  float64
# 13  PREÇO MÉDIO DISTRIBUIÇÃO       120823 non-null  object
# 14  DESVIO PADRÃO DISTRIBUIÇÃO     120823 non-null  object
# 15  PREÇO MÍNIMO DISTRIBUIÇÃO      120823 non-null  object
# 16  PREÇO MÁXIMO DISTRIBUIÇÃO      120823 non-null  object
# 17  COEF DE VARIAÇÃO DISTRIBUIÇÃO  120823 non-null  object
#dtypes: float64(5), int64(1), object(12)
#memory usage: 17.5+ MB
#None


# Selecionando um valor no dataframe
print(df["DATA INICIAL"][2])#imprime 2004-05-09

print(type(df["DATA INICIAL"][2]))#imprime <class 'str'>


# Transformando uma coluna em datetime
df3 = pd.to_datetime(df["DATA INICIAL"])
#print(df3)# vai ser impresso
#0        2004-05-09
#1        2004-05-09
#2        2004-05-09
#3        2004-05-09
#4        2004-05-09
#            ...
#120818   2021-04-25
#120819   2021-04-25
#120820   2021-04-25
#120821   2021-04-25
#120822   2021-04-25
#Name: DATA INICIAL, Length: 120823, dtype: datetime64[ns]

#print(type(df3))# vai ser impresso  <class 'pandas.core.series.Series'>



df["ANO-MES"] = df["DATA FINAL"].apply(lambda x: '{}'.format(x.year))
# (x.year) extraindo o ano
# '{}'.format no formato string
# (lambda x: vai aplicar linha a linha a logica

print(df["ANO-MES"])