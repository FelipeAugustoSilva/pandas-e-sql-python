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