from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import timedelta

from airflow.utils.timezone import datetime

# Note One Operator - One Task (idempotence)
# task id should be unique for the task


with DAG(dag_id='multi_task_dag', start_date=datetime(2021,9,14), schedule_interval="@daily", catchup=False) as dag:
    task_1 = DummyOperator(task_id='task_1', retries=5, retry_delay=timedelta(minutes=5))

    task_2 = DummyOperator(task_id='task_2', retries=5, retry_delay=timedelta(minutes=5))

    task_3 = DummyOperator(task_id='task_3', retries=5, retry_delay=timedelta(minutes=5))

    task_4 = DummyOperator(task_id='task_4', retries=5, retry_delay=timedelta(minutes=5))

    task_5 = DummyOperator(task_id='task_5', retries=5, retry_delay=timedelta(minutes=5))

default_arg = {
    'retries':5, 
    'retry_delay':timedelta(minutes=5)
}

with DAG(dag_id='multi_task_using_defaul_arg_dag', start_date=datetime(2021,9,14), schedule_interval="@daily", catchup=False, default_args=default_arg) as dag:
    task_1 = DummyOperator(task_id='task_1')

    task_2 = DummyOperator(task_id='task_2')

    task_3 = DummyOperator(task_id='task_3')

    task_4 = DummyOperator(task_id='task_4')

    task_5 = DummyOperator(task_id='task_5')