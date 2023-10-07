import logging
import sys
import tempfile
import time
from pprint import pprint

import pendulum

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonVirtualenvOperator, is_venv_installed

log = logging.getLogger(__name__)

PATH_TO_PYTHON_BINARY = sys.executable


with DAG(
    dag_id="example_python_and_pandas",
    schedule=None,
    tags=["example"],
) as dag:

    if not is_venv_installed():
        log.warning("The virtalenv_python example task requires virtualenv, please install it.")
    else:
        # [START howto_operator_python_venv]
        @task.virtualenv(
            task_id="virtualenv_python", requirements=["pandas==2.1.1"], system_site_packages=False
        )
        def pandas_head():
            import pandas as pd
            csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
            df = pd.read_csv(csv_url, index_col=0)
            head = df.head(10)
            return head.to_csv()

        pandas_task = pandas_head()
