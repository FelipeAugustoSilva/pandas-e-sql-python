#Para usar o sqlite3 ele vem instalado com o pacote python padrao, mas precisa instalar a extensão + p 
# extensão SQLITE do alanwyzz
# para mostar o SQLITE EXPLORER, apertar crtl + p digite >>SQLITE: Open Data Base e escolher o database a ser trabalhado
import sqlite3

conn = sqlite3.connect('web1.db')
import pandas as pd

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
print(df_data)
df_data.to_sql('data', conn, index_label='index_name')

c = conn.cursor() # criou o cursor para executar as funções sql
c.execute('CREATE TABLE products (product_id, product_name, price)') # criou a tabela e colunas
conn.commit() # comitou

c.execute('DROP TABLE products') # deletou a tabela

c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)') # criou a tabela, colunas e tipo de dados

# INSERT
c.execute('''INSERT INTO products(product_id, product_name, price)
    VALUES
    (1, 'Computer', 800),
    (2, 'Printer', 200),
    (3, 'Tablet', 300)
''')
conn.commit() # comitou



df_date2 = df_data.iloc[::-2] # df_date2 vai receber o valor de df_data, bagunçada e de tras para frente e vai ser selecionado os valores de 2 em 2
df_date2.to_sql('data', conn, if_exists='append') # inserir o valor do df_date2 na tabela data como append que insere no final da tabela





# SELECT
c.execute("SELECT * FROM data")
c.fetchone() # retorna apenas a primeira linha da tabela
c.fetchall() # Ele retorna cada linha da lista como uma tupla



c.execute("SELECT * FROM data WHERE A > 200") # filtrei a tabela data, para retornar apenas valores acima de 200
df = pd.DataFrame(c.fetchall()) # Criei um dataframe dessa tabela data, com valores acima de 200



query = "SELECT * FROM data"
df = pd.read_sql(query, con=conn, index_col='index_name')



# UPDATE e DELETE
c.execute("UPDATE data SET A=218 WHERE index_name='b'")
conn.commit()

c.execute("UPDATE data SET A=277, B=277 WHERE index_name='b'")
conn.commit()


