from numpy.random import randn
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

print(df.loc[['A', 'B'], 'W']) # vai imprimir os valores da linha A e B na coluna W: 
#A    0.843492
#B   -0.367777
#Name: W, dtype: float64