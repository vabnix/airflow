from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

default_args = {'retries': 5, 'retry_delay': timedelta(minutes=5)}


def _downloading_data():
    print("Entering downloading data function")


def _downloading_data_with_dag_object(**kwargs):
    print(kwargs)

def _downloading_data_execution_date(ds):
    print("Execution Date:" + ds)


def _custom_param_passing(custom_param):
   print("Passing Custom Paramter: ", custom_param)


with DAG(dag_id='using_python_operator_dag',
         start_date=datetime(2021, 9, 14),
         schedule_interval="@daily",
         catchup=False) as dag:
    downloading_data = PythonOperator(task_id='downloading_data',
                                      python_callable=_downloading_data)

with DAG(dag_id='using_python_operator_accessing_dag_object',
         start_date=datetime(2021, 9, 14),
         schedule_interval="@daily",
         catchup=False) as dag:
    downloading_data = PythonOperator(
        task_id='downloading_data',
        python_callable=_downloading_data_with_dag_object
        )


with DAG(dag_id='identify_execution_date_dag', start_date=datetime(2021, 9, 14), schedule_interval="@daily",catchup=False) as dag:
      execution_date = PythonOperator(
          task_id='execution_date',
          python_callable=_downloading_data_execution_date
      )


with DAG(dag_id='passing_own_parameter_dag', start_date=datetime(2021, 9, 14), schedule_interval="@daily",catchup=False) as dag:
      execution_date = PythonOperator(
          task_id='execution_date',
          python_callable=_custom_param_passing,
          op_kwargs={'custom_param':40}
      )