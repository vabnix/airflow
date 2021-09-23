from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.models.baseoperator import cross_downstream

from datetime import datetime, timedelta

default_args = {
    'retries': 5, 
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,
    'email_on_retry': False,
    'email': 'vabnix@hotmail.com'
    }


def _downloading_data_with_dag_object(**kwargs):
    with open('/tmp/my_file.txt', 'w') as f:
        f.write('my_data')
    return 42

def _checking_data(ti):
    my_xcom = ti.xcom_pull(key='return_value', task_ids=['xcom_downloading_data'])
    print(my_xcom)
    print("Inside Checking Data function")

def _failure(context):
    print('========================')
    print('Failure has occured!!')
    print(context)
    print('========================')


with DAG(dag_id='xcom_cross_dependency_dag', 
         start_date=datetime(2021, 9, 14), 
         schedule_interval="@daily", 
         catchup=True) as dag:
    downloading_data = PythonOperator(
        task_id='xcom_downloading_data',
        python_callable=_downloading_data_with_dag_object
    )

    checking_data = PythonOperator(
        task_id='xcom_checking_data',
        python_callable=_checking_data
    )

    waiting_for_data = FileSensor(
       task_id='xcom_waiting_for_data',
       fs_conn_id='fs_default',
       filepath='my_file.txt'
    )

# to recover from failure change exit 1 to exit 0
    processing_data = BashOperator(
        task_id='xcom_processing_data',
        bash_command='exit 1',
        on_failure_callback=_failure
    )

    cross_downstream([downloading_data, checking_data], [waiting_for_data, processing_data])