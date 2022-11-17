import sqlite3

def salvaDados(df):
    #exportando dados do DataFrame em parquet
    #df.to_parquet('result.parquet')

    #Criando e conectando ao banco de dados no sqlite3
    database = "bancodedados.sqlite"
    conn = sqlite3.connect(database)

    # O 'to_sql' exporta o conteúdo do dataframe para o banco Sqlite3
    df.to_sql(name='tabelasql', con=conn, if_exists="append", index=True)

    df.to_csv('tesste.csv')

    conn.close()