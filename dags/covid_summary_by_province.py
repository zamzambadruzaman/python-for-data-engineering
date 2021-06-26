from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import timedelta

project_dir = "/Users/zamzam.badruzaman/PycharmProjects/solution-for-python-for-data-engineering"

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'email': ['admin@idbigdata.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'covid_summary_by_province',
    default_args=default_args,
    description='Covid summary by province',
    schedule_interval='0 3 * * *',
    start_date=days_ago(2),
    tags=['idbigdata'],
) as dag:
    start = DummyOperator(task_id='Start')

    task1 = BashOperator(
        task_id='covid_data_validation',
        bash_command=f'python {project_dir}/validations/covid_data_validations.py',
        dag=dag
    )

    task2 = BashOperator(
        task_id='summary_by_province',
        bash_command=f'python {project_dir}/pipelines/summary_by_province.py',
        dag=dag
    )

    task3 = BashOperator(
        task_id='summary_data_validation',
        bash_command=f'python {project_dir}/validations/summary_by_province_validations.py',
        dag=dag
    )
    end = DummyOperator(task_id='End')

    start >> task1 >> task2 >> task3 >> end
