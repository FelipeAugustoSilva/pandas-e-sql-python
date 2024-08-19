import pandas as pd

caminho_arquivo = 'C:\\Users\\felip\\OneDrive\\Área de Trabalho\\Importante\\Projetos em Python\\asimov\\pandas\\supermarket_sales.csv'


df = pd.read_csv(caminho_arquivo)

print(df.head())