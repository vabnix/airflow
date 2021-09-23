from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {'retries': 5, 'retry_delay': timedelta(minutes=5)}


def _downloading_data_with_dag_object(**kwargs):
    with open('/tmp/my_file.txt', 'w') as f:
        f.write('my_data')


with DAG(dag_id='bash_operator_dag', 
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

    processing_data = BashOperator(
        task_id='processing_data',
        bash_command='exit 0'
    )

# defining dependiency
    # downloading_data.set_downstream(waiting_for_data)
    # waiting_for_data.set_downstream(processing_data)

    # processing_data.set_upstream(waiting_for_data)
    # waiting_for_data.set_upstream(downloading_data)

# another way of performing same task is 
    downloading_data >> waiting_for_data >> processing_data

    ex_downloading_data = PythonOperator(
        task_id='ex_downloading_data',
        python_callable=_downloading_data_with_dag_object
    )

    same_lvl_waiting_for_data = FileSensor(
       task_id='same_waiting_for_data',
       fs_conn_id='fs_default',
       filepath='my_file.txt'
    )

    same_lvl_processing_data = BashOperator(
        task_id='same_processing_data',
        bash_command='exit 0'
    )

# defining data at same level 
    ex_downloading_data >> [ same_lvl_waiting_for_data, same_lvl_processing_data ]