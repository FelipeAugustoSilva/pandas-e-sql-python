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


arr_year = np.arange(gdp_puro['Year'].min(), gdp_puro['Year'].max())
#print(arr_year)
#[1901 1902 1903 1904 1905 1906 1907 1908 1909 1910 1911 1912 1913 1914
# 1915 1916 1917 1918 1919 1920 1921 1922 1923 1924 1925 1926 1927 1928
# 1929 1930 1931 1932 1933 1934 1935 1936 1937 1938 1939 1940 1941 1942
# 1943 1944 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 1956
# 1957 1958 1959 1960 1961 1962 1963 1964 1965 1966 1967 1968 1969 1970
# 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984
# 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998
# 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010]

df_all_years = pd.DataFrame(arr_year, columns=['Year'])
#print(df_all_years)
#     Year
#0    1901
#1    1902
#2    1903
#3    1904
#4    1905
#..    ...
#105  2006
#106  2007
#107  2008
#108  2009
#109  2010

#[110 rows x 1 columns]

df_all_years.index = df_all_years['Year']
#print(df_all_years)
#      Year
#Year
#1901  1901
#1902  1902
#1903  1903
#1904  1904
#1905  1905
#...    ...
#2006  2006
#2007  2007
#2008  2008
#2009  2009
#2010  2010

df_years_off = ~df_all_years['Year'].isin(gdp_puro['Year'])
#print(df_years_off)
#Year
#1901    False
#1902     True
#1903     True
#1904     True
#1905     True
#        ...
#2006    False
#2007     True
#2008     True
#2009     True
#2010     True
#Name: Year, Length: 110, dtype: bool

df_years_off = df_years_off.loc[df_years_off].index
#print(df_years_off)
#Index([1902, 1903, 1904, 1905, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915,
#       1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930,
#       1932, 1933, 1934, 1935, 1937, 1938, 1939, 1940, 1942, 1943, 1944, 1945,
#       1947, 1948, 1949, 1950, 1952, 1953, 1954, 1955, 1957, 1958, 1959, 1960,
#       1962, 1963, 1964, 1965, 1967, 1968, 1969, 1970, 1972, 1973, 1974, 1975,
#       1977, 1978, 1979, 1980, 1982, 1983, 1984, 1985, 1987, 1988, 1989, 1990,
#       1992, 1993, 1994, 1995, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2005,
#       2007, 2008, 2009, 2010],
#      dtype='int64', name='Year')


#print(gdp_puro)
#          Country                                         Region  Year     gdp
#0     Afghanistan  Middle East, North Africa, and Greater Arabia  1901  613.99
#1     Afghanistan  Middle East, North Africa, and Greater Arabia  1906  624.04
#2     Afghanistan  Middle East, North Africa, and Greater Arabia  1911  634.25
#3     Afghanistan  Middle East, North Africa, and Greater Arabia  1916  647.28
#4     Afghanistan  Middle East, North Africa, and Greater Arabia  1921  662.40
#...           ...                                            ...   ...     ...
#4414     Zimbabwe                             Sub-Saharan Africa  1991  782.09
#4415     Zimbabwe                             Sub-Saharan Africa  1996  781.50
#4416     Zimbabwe                             Sub-Saharan Africa  2001  719.96
#4417     Zimbabwe                             Sub-Saharan Africa  2006  520.17
#4418     Zimbabwe                             Sub-Saharan Africa  2011  526.3

gdp_puro = gdp_puro.sort_values(['Country', 'Year'])
#print(gdp_puro)
#          Country                                         Region  Year     gdp
#0     Afghanistan  Middle East, North Africa, and Greater Arabia  1901  613.99
#1     Afghanistan  Middle East, North Africa, and Greater Arabia  1906  624.04
#2     Afghanistan  Middle East, North Africa, and Greater Arabia  1911  634.25
#3     Afghanistan  Middle East, North Africa, and Greater Arabia  1916  647.28
#4     Afghanistan  Middle East, North Africa, and Greater Arabia  1921  662.40
#...           ...                                            ...   ...     ...
#4414     Zimbabwe                             Sub-Saharan Africa  1991  782.09
#4415     Zimbabwe                             Sub-Saharan Africa  1996  781.50
#4416     Zimbabwe                             Sub-Saharan Africa  2001  719.96
#4417     Zimbabwe                             Sub-Saharan Africa  2006  520.17
#4418     Zimbabwe                             Sub-Saharan Africa  2011  526.33

gdp_puro['delta_gdp'] = gdp_puro['gdp'] - gdp_puro['gdp'].shift(1)
gdp_puro['delta_year'] = gdp_puro['Year'] - gdp_puro['Year'].shift(1)
#print(gdp_puro)
#          Country                                         Region  Year     gdp  delta_gdp  delta_year
#0     Afghanistan  Middle East, North Africa, and Greater Arabia  1901  613.99        NaN         NaN
#1     Afghanistan  Middle East, North Africa, and Greater Arabia  1906  624.04      10.05         5.0
#2     Afghanistan  Middle East, North Africa, and Greater Arabia  1911  634.25      10.21         5.0
#3     Afghanistan  Middle East, North Africa, and Greater Arabia  1916  647.28      13.03         5.0
#4     Afghanistan  Middle East, North Africa, and Greater Arabia  1921  662.40      15.12         5.0
#...           ...                                            ...   ...     ...        ...         ...
#4414     Zimbabwe                             Sub-Saharan Africa  1991  782.09      39.79         5.0
#4415     Zimbabwe                             Sub-Saharan Africa  1996  781.50      -0.59         5.0
#4416     Zimbabwe                             Sub-Saharan Africa  2001  719.96     -61.54         5.0
#4417     Zimbabwe                             Sub-Saharan Africa  2006  520.17    -199.79         5.0
#4418     Zimbabwe                             Sub-Saharan Africa  2011  526.33       6.16         5.0

gdp_puro['gdp_year'] = gdp_puro['delta_gdp'] / gdp_puro['delta_year']
#print(gdp_puro)
#          Country                                         Region  Year     gdp  delta_gdp  delta_year  gdp_year
#0     Afghanistan  Middle East, North Africa, and Greater Arabia  1901  613.99        NaN         NaN       NaN
#1     Afghanistan  Middle East, North Africa, and Greater Arabia  1906  624.04      10.05         5.0     2.010
#2     Afghanistan  Middle East, North Africa, and Greater Arabia  1911  634.25      10.21         5.0     2.042
#3     Afghanistan  Middle East, North Africa, and Greater Arabia  1916  647.28      13.03         5.0     2.606
#4     Afghanistan  Middle East, North Africa, and Greater Arabia  1921  662.40      15.12         5.0     3.024
#...           ...                                            ...   ...     ...        ...         ...       ...
#4414     Zimbabwe                             Sub-Saharan Africa  1991  782.09      39.79         5.0     7.958
#4415     Zimbabwe                             Sub-Saharan Africa  1996  781.50      -0.59         5.0    -0.118
#4416     Zimbabwe                             Sub-Saharan Africa  2001  719.96     -61.54         5.0   -12.308
#4417     Zimbabwe                             Sub-Saharan Africa  2006  520.17    -199.79         5.0   -39.958
#4418     Zimbabwe                             Sub-Saharan Africa  2011  526.33       6.16         5.0     1.232

#[4419 rows x 7 columns]

gdp_puro['gdp_year'] = (gdp_puro['delta_gdp'] / gdp_puro['delta_year']).shift(-1)
#print(gdp_puro)
#          Country                                         Region  Year     gdp  delta_gdp  delta_year  gdp_year
#0     Afghanistan  Middle East, North Africa, and Greater Arabia  1901  613.99        NaN         NaN     2.010
#1     Afghanistan  Middle East, North Africa, and Greater Arabia  1906  624.04      10.05         5.0     2.042
#2     Afghanistan  Middle East, North Africa, and Greater Arabia  1911  634.25      10.21         5.0     2.606
#3     Afghanistan  Middle East, North Africa, and Greater Arabia  1916  647.28      13.03         5.0     3.024
#4     Afghanistan  Middle East, North Africa, and Greater Arabia  1921  662.40      15.12         5.0     3.094
#...           ...                                            ...   ...     ...        ...         ...       ...
#4414     Zimbabwe                             Sub-Saharan Africa  1991  782.09      39.79         5.0    -0.118
#4415     Zimbabwe                             Sub-Saharan Africa  1996  781.50      -0.59         5.0   -12.308
#4416     Zimbabwe                             Sub-Saharan Africa  2001  719.96     -61.54         5.0   -39.958
#4417     Zimbabwe                             Sub-Saharan Africa  2006  520.17    -199.79         5.0     1.232
#4418     Zimbabwe                             Sub-Saharan Africa  2011  526.33       6.16         5.0       NaN

#[4419 rows x 7 columns]