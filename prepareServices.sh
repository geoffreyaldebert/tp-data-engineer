mkdir -p pg-airflow
mkdir -p plugins-airflow
cp .envExample .env
echo "AIRFLOW_UID=$(id -u)" >> .env
echo "AIRFLOW_GID=0" >> .env
echo "Done"
