mkdir -p dags-airflow
mkdir -p pg-airflow
mkdir -p plugins-airflow
cp .envExample .env
echo "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" >> .env

