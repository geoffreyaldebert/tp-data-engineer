from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

def test_function_python():
    print(1+2)
        
with DAG(
    dag_id='dag_example',
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example', 'python', 'bash'],
    params={"example_key": "example_value"},
) as dag:

    test_python = PythonOperator(
        task_id="test-python", 
        python_callable=test_function_python
    )

    test_bash = BashOperator(
        task_id='test-bash',
        bash_command='echo 1',
    )


    test_python >> test_bash

