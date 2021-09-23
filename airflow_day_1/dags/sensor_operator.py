from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor

from datetime import datetime, timedelta

default_args = {'retries': 5, 'retry_delay': timedelta(minutes=5)}


def _downloading_data_with_dag_object(**kwargs):
    with open('/tmp/my_file.txt', 'w') as f:
        f.write('my_data')


with DAG(dag_id='file_presense_check_dag', 
         start_date=datetime(2021, 9, 14), 
         schedule_interval="@daily", 
         catchup=False) as dag:
    downloading_data = PythonOperator(
        task_id='downloading_data',
        python_callable=_downloading_data_with_dag_object
    )

    waiting_for_data = FileSensor(
       task_id='waiting_for_data',
       fs_conn_id='fs_default',
       filepath='my_file.txt'
    )
