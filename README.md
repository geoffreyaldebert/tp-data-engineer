# Introduction

The purpose of this interview exercise is to assess your ability to create a data pipeline from scratch.

Your goal is to retrieve some datasets, process them, and then save the results to various types of storages.

We provide a docker-compose which will allow you to deploy different services:
- a mongodb instance (noSQL database - available at localhost:27017)
- a minio instance (storage service compatible with S3 - available at localhost:9000 - user : minioadmin ; password : miniopassword)
- an airflow instance (tool for data engineering pipelines - available at localhost:8080 - user : airflow ; password : airflowpassword)
- a postgres instance (used uniquely by airflow)

There is no need to customize docker-compose.yml, thus you will be able to focus on the data pipeline itself. We provide you with an Airflow in this exercise for your data engineering pipeline, because it is the tool that we use internally, but you are free to use any tool you want (open source please) if you prefer another one.

The result code should be written in Python language. Upon completion, please upload your code on a public git repository and add a README that could help us test your code (don't fork this one for delinking state and results).

After the exercise is completed, we will take the time to discuss what has been done. There's not only one way to do things right, and we're aware of that. Please code what you feel would be naturally elegant and simple for you, not what you think we might expect.

If you're stuck on something, please reach out to us.

## Installation

First, you need to prepare folders and env file in order to deploy your services. Clone this repo, go into it, then :

```
./prepareServices.sh
```

Deploy services :

```
docker-compose up --build -d
```

# Exercise

Etalab team is exporting regularly (every week) the complete list of datasets or organizations hosted in data.gouv.fr. Data is available here: https://www.data.gouv.fr/fr/datasets/catalogue-des-donnees-de-data-gouv-fr/

From these data, you will build a data pipeline which will be scheduled every wednesday at 5PM and will perform:
1) Fetch the list of every dataset in data.gouv.fr
2) Filter this list and keep only those for which the term "mobilité" or "transport" is present
3) Export this list in csv format to a minio bucket called 'datagouv' and in a folder named with current date (YYYY-MM-DD)
4) Filter this list by the popularity of a data producer organization keeping only datasets from TOP 30 organization (you will need the organization list available at https://www.data.gouv.fr/fr/datasets/catalogue-des-donnees-de-data-gouv-fr/ and use the column 'metric.followers' in this csv)
5) Keep only most relevant fields (dataset id, dataset title, dataset followers, organization, organization id, organization followers).
6) Export this list to a mongo document in a database called 'datagouv' and a collection called 'tops'

If you're stuck on something, please reach out to us.

