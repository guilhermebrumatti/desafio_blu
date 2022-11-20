import sqlite3

def salvaDados(df):

    #exportando dados do DataFrame em parquet
    df.to_parquet('result.parquet')

    #conectando ao banco de dados no sqlite3
    database = "bancodedados.sql"
    conn = sqlite3.connect(database)

    #o 'to_sql' exporta o conteúdo do dataframe para o banco Sqlite3, de maneira automática
    df.to_sql(name='tabelasql', con=conn, if_exists="append", index=True)

    #fechando conexão com o banco
    conn.close()