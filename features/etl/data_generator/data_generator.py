from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.operators.empty import EmptyOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from support.callback_functions import success_callback, failure_callback
from support.date_values import DateValues

conn_id = "feature_store"
base_day = DateValues.get_before_one_day()  # 전일(D-1)
airflow_dags_path = Variable.get("AIRFLOW_DAGS_PATH")

with open(f"{airflow_dags_path}/features/etl/data_generator/recipes/01_recipy.sql") as f:
    queries = f.readlines()

with DAG(
        dag_id="etl_data_generator",
        default_args={
            "owner": "mlops.study",
            "depends_on_past": False,
            "email": ["mlops.study@gmail.com"],
            "on_failure_callback": failure_callback,
            "on_success_callback": success_callback,
        },
        description="모델예측_데이터추출",
        schedule="0 8 * * *",
        start_date=datetime(2023, 12, 1),
        catchup=False,
        tags=["mlops", "study"],
) as dag:
    task1 = EmptyOperator(task_id="External_Data_Collection")

    task2 = SQLExecuteQueryOperator(
        task_id="execute_sql_file",
        conn_id=conn_id,
        sql=queries,
        params={'base_day': base_day},
        split_statements=True
    )

    task3 = EmptyOperator(task_id="Load_Data")

    task1 >> task2 >> task3
