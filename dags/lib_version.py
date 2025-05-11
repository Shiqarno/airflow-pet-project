from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='list_installed_packages',
    default_args=default_args,
    schedule_interval=None,  # Trigger manually
    tags=['debug', 'packages'],
) as dag:

    list_packages = BashOperator(
        task_id='list_python_packages',
        bash_command='pip list && echo "✅ Packages listed"'
    )
