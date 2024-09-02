from numpy.random import randn
import numpy as np
import pandas as pd

df = pd.DataFrame(randn(6,4), index=["A", "B", "C", "D", "E","F"], columns="W X Y Z".split())
print(df)# Vai imprimir:
#          W         X         Y         Z
#A -0.069070 -0.828020  0.023329  1.086192
#B  1.093855  0.444584 -0.383135 -1.260967
#C  1.428123  1.515314  0.979667  0.102191
#D  1.469819 -1.334115 -0.224771  0.206432
#E -1.925907 -0.358179  0.371630  0.259834
#F  1.126483  0.130780  1.072153  0.054043

print(df['W'])# Vai imprimir como Series:
#A    1.524107
#B    0.204337
#C    0.741751
#D   -0.428073
#E   -0.596765
#F    2.724441
#Name: W, dtype: float64  // imprime um series

print(df[['W']])# Vai imprimir como Dataframe:
#        W
#A    1.524107
#B    0.204337
#C    0.741751
#D   -0.428073
#E   -0.596765
#F    2.724441
#imprime um dataframe

df['NEW'] = df['W'] #A coluna "NEW" é criada como uma copia da coluna "W"
print(df)# Vai imprimir:
#          W         X         Y         Z       NEW
#A  0.406716  0.689545  0.295687 -0.084293  0.406716
#B  0.923516  0.232737 -0.064267  0.339071  0.923516
#C  0.364242 -1.093986 -0.806543  1.492070  0.364242
#D -1.063641 -0.818737  2.132492 -0.548228 -1.063641
#E  0.002254 -0.347869 -0.772993 -0.613918  0.002254
#F  1.295853  1.026388 -0.004361  1.218345  1.295853

df['NEW'] = df['W'] + df['Y']#A coluna "NEW" é criada como a soma "W" com a "Y"
print(df)# Vai imprimir:
#         W         X         Y         Z       NEW
#A -0.781018  0.380872 -1.000404 -0.867258 -1.781422
#B -0.735584 -1.429580  0.053751 -1.241214 -0.681833
#C  0.161165  0.424863 -1.487678 -1.192123 -1.326513
#D -0.837323  0.989389  0.603416  1.957702 -0.233908
#E  0.223231  0.133178  1.203913  0.456065  1.427145
#F -0.560727  0.560627  0.450339 -0.789515 -0.110387

dfdrop = df.drop('NEW', axis=1) #vai deletar a coluna "NEW", axis=1 referencia a coluna e axios=0 a linnha
print(dfdrop)# Vai imprimir:
#          W         X         Y         Z
#A -0.194198 -0.125839  0.813306  0.479050
#B  0.173949  0.434801 -0.836156 -0.900788
#C -1.036286  0.416714  0.948013 -1.823200
#D -0.955580 -0.485784 -1.635046  0.925374
#E -0.348514  0.456071  2.100620 -1.352052
#F  0.174852  0.339994 -0.652325  0.573187


print(df.loc['A'])#vai retornar toda a linha 'A' como Series # Vai imprimir:
#W      2.100434
#X     -1.241183
#Y     -0.063608
#Z     -0.908290
#NEW    2.036826
#Name: A, dtype: float64

print(df.iloc[0,2])#vai retornar toda o valor da linha 'A' como Series, coluna 'Y':
#-0.32348773618871807

#print(df.loc[['A', 'B'], ['W']]) # vai imprimir os valores da linha A e B na coluna W, como Dataframe: 
print(df.loc[['A', 'B'], 'W']) # vai imprimir os valores da linha A e B na coluna W, como Series: 
#A    0.843492
#B   -0.367777
#Name: W, dtype: float64

print(df.iloc[:-1, :])#vai retornar todas as colunas, excluindo a ultima linha como Series:
#          W         X         Y         Z       NEW
#A  0.303040  0.332996 -1.612914 -1.011123 -1.309874
#B -0.258055  2.159360  0.329679  0.431682  0.071624
#C -1.057510  0.615583 -1.468038 -1.172364 -2.525548
#D  1.801869  1.154607 -1.148270  0.083246  0.653599
#E -1.535369  1.454470 -0.005140  2.153959 -1.540509

print(df.iloc[:-1, 1:])#vai retornar apartir da coluna 1 a ultima e excluindo a ultima linha como Series:
#       X         Y         Z       NEW
#A  0.332996 -1.612914 -1.011123 -1.309874
#B  2.159360  0.329679  0.431682  0.071624
#C  0.615583 -1.468038 -1.172364 -2.525548
#D  1.154607 -1.148270  0.083246  0.653599
#E  1.454470 -0.005140  2.153959 -1.540509


print(df.iloc[1:4, 1:3]) #Vai ser impresso:
#          X         Y
#B -0.546269  0.258595
#C -0.039808 -1.156967
#D  0.450051  0.220546

print(df > 0)#Vai ser impresso:
 #      W      X      Y      Z    NEW
#A   True   True  False   True   True
#B  False   True   True  False  False
#C   True   True  False   True  False
#D  False  False  False   True  False
#E   True  False   True  False   True
#F  False  False  False  False  False

print([df > 0])#Vai ser impresso:
#[       W      X      Y      Z    NEW
#A  False   True   True   True   True
#B  False   True   True  False  False
#C  False  False   True   True  False
#D   True  False  False  False  False
#E   True  False   True  False   True
#F   True  False  False   True  False]

print(df[df > 0])#Vai ser impresso:
#A  0.213293  1.105936       NaN  0.830952       NaN
#B  0.129649  0.109985  0.790409       NaN  0.920058
#C  2.257206       NaN       NaN       NaN  1.469450
#D  0.147148       NaN  0.567944       NaN  0.715092
#E  0.421644       NaN  0.427295  0.450284  0.848939
#F  0.806169       NaN  0.599802       NaN  1.405971

print(df['Y'] > 0)#Vai ser impresso:
#A    False
#B    False
#C    False
#D     True
#E     True
#F     True
#Name: Y, dtype: bool

print(df[df['Y'] > 0])#Vai ser impresso:
#          W         X         Y         Z       NEW
#A -0.148982 -0.970510  0.640662 -0.380043  0.491680
#B  1.712953 -0.456111  1.511011 -0.643244  3.223965
#E -0.639533  0.148702  0.265175 -0.869425 -0.374358

print(df[(df['Y'] > 0) & (df['W'] > 0)])#Vai ser impresso:
#          W         X         Y         Z       NEW
#A  0.794655  0.246239  0.576488 -0.063305  1.371143
#D  0.058178  2.110317  1.766410  0.367221  1.824588

print(df.index)#Vai ser impresso:
#Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

print(df.columns)#Vai ser impresso:
#Index(['W', 'X', 'Y', 'Z', 'NEW'], dtype='object')

print(df.reset_index())#Vai ser impresso:
#  index         W         X         Y         Z       NEW
#0     A  1.060136  0.180986 -0.677070  0.371606  0.383066
#1     B  0.872019  0.631747  0.131642  1.164056  1.003661
#2     C  0.564020 -1.541185 -0.948285 -0.570357 -0.384264
#3     D -0.693352  2.309862 -0.647985 -0.020777 -1.341336
#4     E  0.266104  0.468459 -1.389096 -0.302861 -1.122992
#5     F  0.843078  0.204167  0.733816 -0.121887  1.576894

#print(df.reset_index(inplace=True))#Vai ser aplicado a alteração na tabela, e vai ser impresso:
#  index         W         X         Y         Z       NEW
#0     A  1.060136  0.180986 -0.677070  0.371606  0.383066
#1     B  0.872019  0.631747  0.131642  1.164056  1.003661
#2     C  0.564020 -1.541185 -0.948285 -0.570357 -0.384264
#3     D -0.693352  2.309862 -0.647985 -0.020777 -1.341336
#4     E  0.266104  0.468459 -1.389096 -0.302861 -1.122992
#5     F  0.843078  0.204167  0.733816 -0.121887  1.576894

#print(df.set_index, inplace=True)#Vai retornar a o indice antigo, e vai ser impresso:
#  index         W         X         Y         Z       NEW
#     A  1.060136  0.180986 -0.677070  0.371606  0.383066
#     B  0.872019  0.631747  0.131642  1.164056  1.003661
#     C  0.564020 -1.541185 -0.948285 -0.570357 -0.384264
#     D -0.693352  2.309862 -0.647985 -0.020777 -1.341336
#     E  0.266104  0.468459 -1.389096 -0.302861 -1.122992
#     F  0.843078  0.204167  0.733816 -0.121887  1.576894

novoind = 'CA NY WY OR CO TX'. split()
print(novoind)# vai ser impresso:
#['CA', 'NY', 'WY', 'OR', 'CO']

df["novo_index"] = novoind
print(df)# vai ser impresso:
#          W         X         Y         Z       NEW novo_index
#A  0.775198 -1.053677 -0.981476  0.084360 -0.206278         CA
#B  0.246798 -0.373893  0.682040  0.411696  0.928838         NY
#C -0.661235 -0.537188 -0.966970 -0.017912 -1.628206         WY
#D -1.399793  2.347661 -0.904554  1.969039 -2.304347         OR
#E  0.688199  0.698024 -2.005767 -0.059245 -1.317568         CO
#F  0.628412  0.079690  0.265340 -0.443040  0.893752         TX

print(df.set_index("novo_index")) #vai ser impresso:
#                   W         X         Y         Z       NEW
#novo_index
#CA          0.049143  0.569200  0.755003 -0.594121  0.804146
#NY         -0.378504  0.925384 -0.154997 -1.766625 -0.533501
#WY          0.061011 -0.206615  1.277634  0.038495  1.338645
#OR          0.846184 -0.658281  0.579789 -1.182950  1.425973
#CO         -0.434926  0.531408  0.341305 -0.741673 -0.093621
#TX          0.773267  0.306049  0.528435 -1.551062  1.301702

print(df.reset_index().set_index("novo_index")) #vai ser impresso:
#           index         W         X         Y         Z       NEW
#novo_index
#CA             A  0.035387  2.125692 -1.369107 -0.515017 -1.333720
#NY             B -0.215156  1.427612 -1.675568  0.818116 -1.890724
#WY             C -0.078143  1.789825  0.608293 -1.166089  0.530149
#OR             D  1.703278 -2.108511 -1.335699 -1.105491  0.367579
#CO             E -0.334299  1.851096 -0.188787 -0.430120 -0.523086
#TX             F -1.090490  0.906270  1.651790  1.125886  0.561301


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
print(hier_index) #Vai ser impresso uma tupla:
#[('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index) #Vai ser impresso:
#MultiIndex([('G1', 1),
#            ('G1', 2),
#           ('G1', 3),
#           ('G2', 1),
#            ('G2', 2),
#            ('G2', 3)],
#           )

dff = pd.DataFrame(np.random.randn(6,2),index=hier_index, columns=['A', 'B'])
print(dff)#Vai ser impresso o dataframe assim:
#             A         B
#G1 1  0.320152  1.488853
#   2 -0.324630  1.279359
#   3 -0.993763 -2.207344
#G2 1 -0.397826 -0.778301
#   2 -0.899567 -1.159682
#   3 -0.011167  0.546462

dff.index.names = ['Grupo', 'Numero']
print(dff)#Vai ser impresso  assim:
#                     A         B
#Grupo Numero
#G1    1      -0.066932 -1.413828
#      2      -1.271939  0.881977
#      3      -0.334779  0.058210
#G2    1       1.158361  0.670691
#      2      -2.142515 -0.376607
#      3       0.461618  1.917577



print(dff.loc["G1"])#Vai ser impresso o dataframe assim:
#          A         B
#1 -0.482768  1.484198
#2  0.114278 -1.226552
#3 -0.158794 -0.650002

print(dff.loc["G1"].loc[1])#Vai ser impresso assim:
#A   -0.201618
#B   -0.246084
#Name: 1, dtype: float64


print(dff.xs(1, level='Numero'))#Vai ser impresso  assim:
#              A         B
#Grupo
#G1     1.887206  0.371498
#G2     1.307078 -0.199035


dfff = pd.DataFrame({'A': [1,2,np.nan],
                    'B': [5,np.nan,np.nan],
                    'C': [1,2,3]})

print(dfff) #vai ser impresso: 
#     A    B  C
#0  1.0  5.0  1
#1  2.0  NaN  2
#2  NaN  NaN  3

#print(dfff.dropna(axis=0))
print(dfff.dropna())# vai ser excluido as linhas que possuam valores em NaN:
#     A    B  C
#0  1.0  5.0  1

print(dfff.dropna(axis=1))# vai ser excluido as colunas que possuam valores iguais a NaN:
#   C
#0  1
#1  2
#2  3

print(dfff.dropna(axis=1, thresh=2))# Vai escluir apenas as colunas com 2 ou mais valores com NaN:
 #    A  C
#0  1.0  1
#1  2.0  2
#2  NaN  3

print(dfff.fillna(0)) # os valores em NaN seram substituidos por 0, podendo usar até strings:
#     A    B  C
#0  1.0  5.0  1
#1  2.0  0.0  2
#2  0.0  0.0  3