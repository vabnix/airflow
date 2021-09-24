from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.timezone import datetime

default_args = {
    'retries': 5, 
    'retry_delay': timedelta(minutes=5)
    }

def _calling_t1_ops():
    print('Inside T1 Operation')

def _calling_t2_ops():
    print('Inside T2 Operation')


def _calling_t3_ops():
    print('Inside T3 Operation')


def _calling_t4_ops():
    print('Inside T4 Operation')

def _calling_t5_ops():
    print('Inside T5 Operation')

with DAG(dag_id='default_executor_dag', 
         start_date=datetime(2021, 9, 14), 
         schedule_interval="@daily", 
         catchup=False) as dag:
         t1_data = PythonOperator(
             task_id='t1',
             python_callable=_calling_t1_ops
         )

         t2_data = PythonOperator(
             task_id='t2',
             python_callable=_calling_t2_ops
         )

         t3_data = PythonOperator(
             task_id='t3',
             python_callable=_calling_t3_ops
         )

         t4_data = PythonOperator(
             task_id='t4',
             python_callable=_calling_t4_ops
         )

         t5_data = PythonOperator(
             task_id='t5',
             python_callable=_calling_t5_ops
         )

         t1_data.set_downstream(t2_data)
         t2_data.set_downstream(t4_data)

         t1_data.set_downstream(t3_data)
         t3_data.set_downstream(t4_data)

         t4_data.set_downstream(t5_data)
