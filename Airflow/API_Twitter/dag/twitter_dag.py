import sys
sys.path.append("airflow_pipeline")

from airflow.models import DAG
from datetime import datetime, timedelta
from operators.twitter_operator import TwitterOperator
from os.path import join   
from airflow.utils.dates import days_ago

sys.path.append("airflow_pipeline")

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"

query = "data science"

with DAG(dag_id="Twitter_dag", start_date=days_ago=(2), schedule_interval="@daily") as dag:
        to = TwitterOperator(file_path=join("Datalake/twitter_datascience",
                                            "extract_date={{ ds }}",
                                            "datascience_{{ ds_nodash }}.json"),
                                            query=query, start_time="{{data_interval_start.strtime('%Y-%m-%dT%H:%M:%S.00Z')}}",
                                            end_time="{{ data_interval_end.strtime('%Y-%m-%dT%H:%M:%S.00Z')}}", tasl_id = "twitter_datascience")
