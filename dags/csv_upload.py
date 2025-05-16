import os
import glob
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator

import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, Text, TIMESTAMP

def upload_csv_to_postgres_via_airflow(
    table_name: str,
    folder_path: str,
    postgres_conn_id: str = "postgres_default"
):    
    # 1. Get connection from Airflow
    conn = BaseHook.get_connection(postgres_conn_id)
    db_url = f"postgresql+psycopg2://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"

    # 2. Define table schema
    engine = create_engine(db_url)
    metadata = MetaData()

    table = Table(table_name, metadata,
        Column('id', Integer, primary_key=True),
        Column('date', TIMESTAMP, nullable=False),
        Column('amount', Float, nullable=False),
        Column('comment', Text),
    )

    # 3. Create table if it doesn't exist
    metadata.create_all(engine, checkfirst=True)

    # 4. Check if folder exists and get CSV files
    if os.path.isdir(folder_path):
        csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
        # Check if there are CSV files to process
        for file_path in csv_files:
            # 4.1 Read CSV file
            df = pd.read_csv(file_path, parse_dates=['date'])

            # 4.2 Insert data
            df.to_sql(table_name, con=engine, if_exists='append', index=False, method='multi')
            print(f"✅ Uploaded {len(df)} rows into table '{table_name}' from {file_path}.")

            # 4.3 Move processed file to archive
            archive_path = file_path.replace("incoming", "archive")  
            os.rename(file_path, archive_path) 
            print(f"✅ Moved {file_path} to {archive_path}.")

# Example DAG
default_args = {'start_date': datetime(2024, 1, 1), 'catchup': False}
with DAG('csv_to_postgres_sqlalchemy_dag',
         default_args=default_args,
         schedule_interval=None,
         tags=['example']) as dag:

    upload_task = PythonOperator(
        task_id='upload_csv',
        python_callable=upload_csv_to_postgres_via_airflow,
        op_kwargs={
            'table_name': 'raw_transaction_data',
            'folder_path': '/opt/airflow/data/incoming/',
            'postgres_conn_id': 'postgres_default'
        }
    )
