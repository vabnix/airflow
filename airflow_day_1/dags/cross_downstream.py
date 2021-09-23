from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import cross_downstream

from datetime import datetime, timedelta

default_args = {'retries': 5, 'retry_delay': timedelta(minutes=5)}


def _downloading_data_with_dag_object(**kwargs):
    with open('/tmp/my_file.txt', 'w') as f:
        f.write('my_data')

def _checking_data():
    print("Inside Checking Data function")


with DAG(dag_id='cross_dependency_dag', 
         start_date=datetime(2021, 9, 14), 
         schedule_interval="@daily", 
         catchup=False) as dag:
    downloading_data = PythonOperator(
        task_id='downloading_data',
        python_callable=_downloading_data_with_dag_object
    )

    checking_data = PythonOperator(
        task_id='checking_data',
        python_callable=_checking_data
    )

    waiting_for_data = FileSensor(
       task_id='waiting_for_data',
       fs_conn_id='fs_default',
       filepath='my_file.txt'
    )

    processing_data = BashOperator(
        task_id='processing_data',
        bash_command='exit 0'
    )

    cross_downstream([downloading_data, checking_data], [waiting_for_data, processing_data])