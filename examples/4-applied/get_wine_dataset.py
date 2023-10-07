import logging

from datetime import datetime
from airflow import DAG, Dataset
from airflow.decorators import task
from airflow.operators.python import is_venv_installed

log = logging.getLogger(__name__)

RAW_WINE_DATASET = Dataset("file://localhost/airflow/datasets/raw_wine_dataset.csv")

with DAG(
    dag_id="wine_dataset_get",
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=["example"],
) as dag:

    if not is_venv_installed():
        raise RuntimeError("virtualenv is not installed!")
    else:
        @task.virtualenv(
            task_id="virtualenv_python", requirements=["pandas==2.1.1"],
            system_site_packages=False, outlets=[RAW_WINE_DATASET]
        )
        def retrieve_dataset():
            import pandas as pd
            df = pd.read_csv("https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv", index_col=0)
            df.to_csv("~/airflow/datasets/raw_wine_dataset.csv")

        retrieve_dataset()
