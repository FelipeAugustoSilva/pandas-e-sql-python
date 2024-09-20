import pandas as pd


# Concatenando dois dataframes
df1 = pd.read_csv("gasolina_2000+.csv", index_col=0) #Estou lendo o csv e dizendo que o index é a coluna 0
df2 = pd.read_csv("gasolina_2010+.csv", index_col=0) #Estou lendo o csv e dizendo que o index é a coluna 0

df = pd.concat([df1, df2]) # concatenando o df1 com df2

df_mes_ano = pd.DataFrame(df)
# Converter a coluna 'DATA INICIAL' para datetime
df_mes_ano['DATA INICIAL'] = pd.to_datetime(df_mes_ano['DATA INICIAL'])
# Criar a nova coluna 'ANO-MES' com o formato YYYY-MM
df_mes_ano['ANO-MES'] = df_mes_ano['DATA INICIAL'].dt.strftime('%Y-%m')




#print(df_mes_ano.columns)
#Index(['DATA INICIAL', 'DATA FINAL', 'REGIÃO', 'ESTADO', 'PRODUTO',
#       'NÚMERO DE POSTOS PESQUISADOS', 'UNIDADE DE MEDIDA',
#       'PREÇO MÉDIO REVENDA', 'DESVIO PADRÃO REVENDA', 'PREÇO MÍNIMO REVENDA',
#      'PREÇO MÁXIMO REVENDA', 'MARGEM MÉDIA REVENDA',
#       'COEF DE VARIAÇÃO REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO',
#       'DESVIO PADRÃO DISTRIBUIÇÃO', 'PREÇO MÍNIMO DISTRIBUIÇÃO',
#       'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO', 'ANO-MES'],
#      dtype='object')

#print(df_mes_ano['PRODUTO'].value_counts())
#GASOLINA COMUM        23570
#GLP                   23561
#ETANOL HIDRATADO      23440
#ÓLEO DIESEL           21194
#GNV                   14469
#ÓLEO DIESEL S10        9113
#OLEO DIESEL S10        2376
#OLEO DIESEL            2351
#GASOLINA ADITIVADA      749
#Name: count, dtype: int64


df_filtro = df_mes_ano[df_mes_ano['PRODUTO'] == 'GASOLINA COMUM']
#print(df_filtro)
#       DATA INICIAL  DATA FINAL        REGIÃO  ... PREÇO MÍNIMO DISTRIBUIÇÃO PREÇO MÁXIMO DISTRIBUIÇÃO  COEF DE VARIAÇÃO DISTRIBUIÇÃO
#12064    2004-05-09  2004-05-15  CENTRO OESTE  ...                     1.651                    1.7427                          0.012
#12065    2004-05-09  2004-05-15  CENTRO OESTE  ...                    1.6643                     1.915                          0.021
#12066    2004-05-09  2004-05-15  CENTRO OESTE  ...                      1.75                    2.0713                          0.036
#12067    2004-05-09  2004-05-15  CENTRO OESTE  ...                   1.70701                    1.9703                          0.018
#12068    2004-05-09  2004-05-15      NORDESTE  ...                    1.6789                     1.918                          0.024
#...             ...         ...           ...  ...                       ...                       ...                            ...
#120721   2021-04-25  2021-05-01         NORTE  ...                  -99999.0                  -99999.0                       -99999.0
#120722   2021-04-25  2021-05-01           SUL  ...                  -99999.0                  -99999.0                       -99999.0
#120723   2021-04-25  2021-05-01       SUDESTE  ...                  -99999.0                  -99999.0                       -99999.0
#120724   2021-04-25  2021-05-01      NORDESTE  ...                  -99999.0                  -99999.0                       -99999.0
#120725   2021-04-25  2021-05-01         NORTE  ...                  -99999.0                  -99999.0                       -99999.0
#[23570 rows x 18 columns]

df_filtro = df_filtro[df_mes_ano['ANO-MES'] == '2008-08']
#print(df_filtro)
#      DATA INICIAL  DATA FINAL        REGIÃO              ESTADO  ... PREÇO MÍNIMO DISTRIBUIÇÃO  PREÇO MÁXIMO DISTRIBUIÇÃO COEF DE VARIAÇÃO DISTRIBUIÇÃO  ANO-MES
#17976   2008-08-03  2008-08-09  CENTRO OESTE    DISTRITO FEDERAL  ...                    2.0968                        2.3                         0.023  2008-08      
#17977   2008-08-03  2008-08-09  CENTRO OESTE               GOIAS  ...                      2.12                     2.3322                         0.019  2008-08      
#17978   2008-08-03  2008-08-09  CENTRO OESTE         MATO GROSSO  ...                    2.1959                        2.5                         0.031  2008-08      
#17979   2008-08-03  2008-08-09  CENTRO OESTE  MATO GROSSO DO SUL  ...                    2.1632                       2.47                         0.023  2008-08      
#17980   2008-08-03  2008-08-09      NORDESTE             ALAGOAS  ...                    2.1694                      2.397                         0.025  2008-08      
#...            ...         ...           ...                 ...  ...                       ...                        ...                           ...      ...      
#18106   2008-08-31  2008-09-06       SUDESTE      RIO DE JANEIRO  ...                    2.1651                     2.4808                         0.026  2008-08      
#18107   2008-08-31  2008-09-06       SUDESTE           SAO PAULO  ...                     1.949                     2.2677                         0.021  2008-08      
#18108   2008-08-31  2008-09-06           SUL              PARANA  ...                     1.964                     2.2448                         0.021  2008-08      
#18109   2008-08-31  2008-09-06           SUL   RIO GRANDE DO SUL  ...                     2.068                     2.3909                         0.023  2008-08      
#18110   2008-08-31  2008-09-06           SUL      SANTA CATARINA  ...                     2.057                     2.3312                         0.023  2008-08 


df_filtro = df_filtro[df_mes_ano['ANO-MES'] == '2008-08']['PREÇO MÉDIO REVENDA'].mean()
#print(df_filtro)
#2.6062888888888893



df_filtro = df_mes_ano[(df_mes_ano['ANO-MES'] == '2008-08') & (df_mes_ano['ESTADO'] == 'SAO PAULO')]['PREÇO MÉDIO REVENDA'].mean()
#print(df_filtro)
#7.81584


df_filtro2 = df_mes_ano[df_mes_ano['PREÇO MÉDIO REVENDA'] > 5][['ESTADO', 'ANO-MES', 'PREÇO MÉDIO REVENDA']]
#print(df_filtro2)
#                    ESTADO  ANO-MES  PREÇO MÉDIO REVENDA
#4132     DISTRITO FEDERAL  2004-05               33.989
#24133                GOIAS  2004-05               30.335
#24134          MATO GROSSO  2004-05               38.568
#24135   MATO GROSSO DO SUL  2004-05               33.388
#24136              ALAGOAS  2004-05               32.391
#...                    ...      ...                  ...
#120750           SAO PAULO  2021-04               85.340
#120751             SERGIPE  2021-04               83.508
#120752           TOCANTINS  2021-04               93.867
#120769                ACRE  2021-04                5.550
#120796                ACRE  2021-04                5.209

#[24304 rows x 3 columns]     07:38

df_filtro2 = df_mes_ano[df_mes_ano['PREÇO MÉDIO REVENDA'] > 5][['ESTADO', 'ANO-MES', 'PREÇO MÉDIO REVENDA']].head(20)
#print(df_filtro2)
#                    ESTADO  ANO-MES  PREÇO MÉDIO REVENDA
#24132     DISTRITO FEDERAL  2004-05               33.989
#24133                GOIAS  2004-05               30.335
#24134          MATO GROSSO  2004-05               38.568
#24135   MATO GROSSO DO SUL  2004-05               33.388
#24136              ALAGOAS  2004-05               32.391
#24137                BAHIA  2004-05               32.856
#24138                CEARA  2004-05               32.778
#24139             MARANHAO  2004-05               33.141
#24140              PARAIBA  2004-05               34.860
#24141           PERNAMBUCO  2004-05               32.897
#24142                PIAUI  2004-05               35.143
#24143  RIO GRANDE DO NORTE  2004-05               31.029
#24144              SERGIPE  2004-05               32.625
#24145                 ACRE  2004-05               39.328
#24146                AMAPA  2004-05               31.840
#24147             AMAZONAS  2004-05               31.036
#24148                 PARA  2004-05               32.194
#24149             RONDONIA  2004-05               35.543
#24150              RORAIMA  2004-05               33.743
#24151            TOCANTINS  2004-05               33.271



# Converter a coluna 'DATA FINAL' para datetime
df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'], errors='coerce')
# Filtrar para o ano de 2012
df_filtro3 = df[df['DATA FINAL'].dt.year == 2012]
# Filtrar para a região 'SUL' e calcular a média de 'PREÇO MÉDIO REVENDA'
media_preco_sul = df_filtro3[df_filtro3['REGIÃO'] == 'SUL']['PREÇO MÉDIO REVENDA'].mean()
#print(media_preco_sul)
#9.842052564102564

# Cria a coluna mes com base  no mes da data final
df['MES'] = df['DATA FINAL'].apply(lambda x: x.month)
# Filtra a coluna Estado por RIO de JANEIRO
df_rio = df[df['ESTADO'] == 'RIO DE JANEIRO']
# Converte a coluna DATA INICIAL em datetime
df_rio['DATA INICIAL'] = pd.to_datetime(df_rio['DATA INICIAL'])
# Criar a nova coluna 'ANO-MES' com o formato YYYY-MM
df_rio['ANO-MES'] = df_rio['DATA INICIAL'].dt.strftime('%Y-%m')
#Agrupa o datafame por ano mes, PRECO MEDIO e MES
#print(df_rio.groupby('ANO-MES')[['PREÇO MÉDIO REVENDA', 'MES']].last())
#         PREÇO MÉDIO REVENDA  MES
#ANO-MES
#2004-05                1.368    6
#2004-06                1.462    7
#2004-07                1.461    7
#2004-08                1.466    9
#2004-09                1.466   10
#...                      ...  ...
#2020-12                3.825    1
#2021-01                3.890    2
#2021-02                4.356    3
#2021-03                4.370    4
#2021-04                4.302    5

#[203 rows x 2 columns]

df_month_rio = df_rio.groupby('ANO-MES')[['PREÇO MÉDIO REVENDA', 'MES']].last()
#print(df_month_rio[df_month_rio['MES'] == 12])
#         PREÇO MÉDIO REVENDA  MES
#ANO-MES
#2004-11                1.614   12
#2005-11                1.819   12
#2005-12                1.821   12
#2006-11                1.807   12
#2007-11                1.811   12
#2008-11                2.082   12
#2009-11                1.992   12
#2010-11                1.983   12
#2011-11                2.009   12
#2011-12                2.007   12
#2012-11                2.111   12
#2014-11                1.787   12
#2015-11                2.107   12
#2016-11                2.116   12
#2016-12                2.067   12
#2017-11                2.263   12
#2018-11                3.085   12
#2020-11                3.708   12

#print((df_month_rio[df_month_rio['MES'] == 12] / df_month_rio[df_month_rio['MES'] == 12].shift(1) - 1) * 100)

#         PREÇO MÉDIO REVENDA  MES
#ANO-MES
#2004-11                  NaN  NaN
#2005-11            12.701363  0.0
#2005-12             0.109951  0.0
#2006-11            -0.768808  0.0
#2007-11             0.221361  0.0
#2008-11            14.964108  0.0
#2009-11            -4.322767  0.0
#2010-11            -0.451807  0.0
#2011-11             1.311145  0.0
#2011-12            -0.099552  0.0
#2012-11             5.181863  0.0
#2014-11           -15.348176  0.0
#2015-11            17.907107  0.0
#2016-11             0.427148  0.0
#2016-12            -2.315690  0.0
#2017-11             9.482342  0.0
#2018-11            36.323464  0.0
#2020-11            20.194489  0.0

df_max = df_rio.groupby("ANO-MES").max()["PREÇO MÉDIO REVENDA"] #Agrupa os valores por ANO-MES e retorna o maior valor PREÇO MEDIO REVENDA
#print(df_max)
#2004-05    29.154
#2004-06    29.238
#2004-07    29.344
#2004-08    29.363
#2004-09    29.138
#            ...
#2020-12    67.210
#2021-01    70.217
#2021-02    71.034
#2021-03    74.574
#2021-04    76.847
#Name: PREÇO MÉDIO REVENDA, Length: 203, dtype: float64

df_min = df_rio.groupby("ANO-MES").min()["PREÇO MÉDIO REVENDA"] #Agrupa os valores por ANO-MES e retorna o menor valor PREÇO MEDIO REVENDA
#print(df_min) 
#ANO-MES
#2004-05    1.092
#2004-06    1.100
#2004-07    1.102
#2004-08    1.101
#2004-09    1.104
#           ...
#2020-12    3.007
#2021-01    3.025
#2021-02    3.043
#2021-03    3.091
#2021-04    3.011
#Name: PREÇO MÉDIO REVENDA, Length: 203, dtype: float64

df_diff = pd.DataFrame() # Cria um dataframe vazio
df_diff["abs_diff"] = df_max - df_min #Cria uma coluna abs_diff e preenche com a diferença entre df_max e df_min
#print(df_diff)
#         abs_diff
#ANO-MES
#2004-05    28.062
#2004-06    28.138
#2004-07    28.242
#2004-08    28.262
#2004-09    28.034
#...           ...
#2020-12    64.203
#2021-01    67.192
#2021-02    67.991
#2021-03    71.483
#2021-04    73.836

#[203 rows x 1 columns]

df_diff["percent_diff"] = (df_max - df_min) / df_min * 100 #Cria uma coluna percent_diff e preenche com a diferença entre df_max e df_min em percentual
#print(df_diff)
#         abs_diff  percent_diff
#ANO-MES
#2004-05    28.062   2569.780220
#2004-06    28.138   2558.000000
#2004-07    28.242   2562.794918
#2004-08    28.262   2566.939146
#2004-09    28.034   2539.311594
#...           ...           ...
#2020-12    64.203   2135.118058
#2021-01    67.192   2221.223140
#2021-02    67.991   2234.341111
#2021-03    71.483   2312.617276
#2021-04    73.836   2452.208569

#[203 rows x 2 columns]