from airflow.models.baseoperator import ScheduleInterval
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

with DAG(dag_id='simple_dag', start_date=datetime(2021, 1, 1), schedule_interval="*/10 * * * *") as dag:
    task_1 = DummyOperator(task_id='task_1')

with DAG(dag_id='specific_hour_dag_using_timedelta', start_date=datetime(2021, 9, 13), schedule_interval=timedelta(hours=7)) as dag:
    task_1 = DummyOperator(task_id='task_1')



with DAG(dag_id='daily_dag_using_timedelta', start_date=datetime(2021, 9, 13), schedule_interval=timedelta(days=1)) as dag:
    task_1 = DummyOperator(task_id='task_1')

with DAG(dag_id='weekly_dag_using_timedelta', start_date=datetime(2021, 9, 13), schedule_interval=timedelta(days=7)) as dag:
    task_1 = DummyOperator(task_id='task_1')

with DAG(dag_id='no_schedule_dag', start_date=datetime(2021,9,13), schedule_interval='@daily') as dag:
    print("No schedule dag is active now")
    task_1 = DummyOperator(task_id='task_1')
    print("Dummy task was triggered")


with DAG(dag_id='backfill_non_triggered_dag', 
    start_date=days_ago(3), 
    catchup=True) as dag:
    task_1 = DummyOperator(task_id='task_1')

# Way to start the past dags without using catchup, by doing so it will only run for actively triggered dags, so it will not run for past days
# By setting catchup to false only the latest non triggered dags runs will be triggered
with DAG(dag_id='backfill_without_catchup_dag', 
    start_date=days_ago(3), 
    catchup=False) as dag:
    task_1 = DummyOperator(task_id='task_1')


# max_active_runs defined the max number of dags running allowed for active runs for specific dags
with DAG(dag_id='max_active_run_dag', start_date=days_ago(3), schedule_interval="@daily", catchup=False, max_active_runs=3) as dag:
    task_1 = DummyOperator(task_id='task_1')