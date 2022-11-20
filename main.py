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

    #formatando as datas das colunas created e edited
    df['created'] = pd.to_datetime(df['created'])
    df['created'] = df['created'].dt.strftime('%d/%m/%Y %H:%M')

    df['edited'] = pd.to_datetime(df['edited'])
    df['edited'] = df['edited'].dt.strftime('%d/%m/%Y %H:%M')

    df.to_csv('text.csv')

    #executando a funcao salvaDados do arquivo data_save.py, passando o dataframe como parâmetro
    salvaDados(df)

with DAG('STARWARS_DATA', schedule='@daily', start_date=datetime(2022, 1, 1), catchup=False) as dag:

    t1 = PythonOperator(
    task_id="Task_puxadados",
    python_callable=app_func
    )

    t1