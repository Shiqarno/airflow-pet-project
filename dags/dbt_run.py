from airflow import DAG
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator
from datetime import datetime

with DAG(
    'dbt_plugin_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    dbt_run = DbtRunOperator(
        task_id='dbt_run',
        dir='/opt/airflow/.dbt',
        profiles_dir='/opt/airflow/.dbt'
    )

    dbt_test = DbtTestOperator(
        task_id='dbt_test',
        dir='/opt/airflow/.dbt',
        profiles_dir='/opt/airflow/.dbt'
    )

    dbt_run >> dbt_test
