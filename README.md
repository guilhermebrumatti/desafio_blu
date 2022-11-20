# DESAFIO BLU

Este é o desafio proposto pela Blu.

Nele foram aplicados conhecimentos de:<br><br>
-Python<br>
-Docker<br>
-AirFlow<br>
-Banco de dados<br><br>

# 1- CÓDIGO<br>

```
import pandas as pd
from data_save import salvaDados
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow import DAG

def app_func():
    #consultando url e transformando resultado em DataFrame
    df = pd.read_json('https://swapi.dev/api/films/?format=json')
    df.drop('count', axis=1, inplace=True)
    df.drop('next', axis=1, inplace=True)
    df.drop('previous', axis=1, inplace=True)
    df = pd.DataFrame(df['results'].values.tolist(), index=df.index)
    df = df.applymap(str)
```

O código inicia a leitura dos dados(JSON) direto da url e armazena na variável df através do Pandas<br>
Depois segue com exclusão das colunas indesejadas.

```
#formatando as datas das colunas created e edited
    df['created'] = pd.to_datetime(df['created'])
    df['created'] = df['created'].dt.strftime('%d/%m/%Y %H:%M')

    df['edited'] = pd.to_datetime(df['edited'])
    df['edited'] = df['edited'].dt.strftime('%d/%m/%Y %H:%M')

    #executando a funcao salvaDados do arquivo data_save.py, passando o dataframe como parâmetro
    salvaDados(df)
```

No trecho acima, o código trata as colunas **created** e **edited**, deixando as informações mais legíveis.<br>
Depois o DataFrame é enviado para o arquivo **data_save.py** através da variável **df**

```
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
```

O arquivo **save_data.py** recebe o **DataFrame** e:<br>
1- Exporta para .parquet<br>
2- Cria o banco de dados através do sqlite3 e cria a conexão com ele<br>
3- Cria uma tabela chamada **tabelasql**(caso a tabela já exista, os dados do DataFrame serão incrementados na tabela) no banco de dados e exporta o DataFrame para a tabela<br>
4- Fecha a conexão com o banco de dados<br>

```
#definindo DAG para que rode a aplicação uma vez ao dia
with DAG('STARWARS_DATA', schedule='@daily', start_date=datetime(2022, 1, 1), catchup=False) as dag:

    t1 = PythonOperator(
    task_id="Task_puxadados",
    python_callable=app_func
    )

    t1
```

O trecho acima está no fim do arquivo **main.py**<br>
Ele é lido pelo AirFlow para que a aplicação possa ser orquestrada pelo AirFlow.<br>
A DAG é chamada de **STARWARS_DATA** e deve ser executada pelo AirFlow uma vez por dia.<br>
Uma task chamada **Task_puxadados** é criada afim de executar a função **app_func()**, que dará início ao processo de extração dos dados.<br>
