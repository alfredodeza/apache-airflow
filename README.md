# Learning Apache Airflow

Apache Airflow is a platform to define data pipelines, monitor execution and handle workflow orchestration. If you are familiar with schedulers, consumers, and queues, Airflow is a great tool to explore.

Airflow solves several problems like managing scheduled jobs and easily handling dependencies between tasks. It also provides a great UI to monitor and manage the workflows.

This repository is part of a course on applied Apache Airflow. It is meant to be used as a reference for the course and not as a standalone guide. 

## Lesson 1: Installation

There are many different ways you can install and use Airflow. From building the project from source to using a hosted (ready-to-use) service. In this course we will explore installing from the Python Package Index (PyPI) as well as using Docker Compose. 

* [Installing from PyPI](./examples/1-pip/)
* [Installing with Docker Compose](./examples/2-compose/)

### PyPI

Always refer to the [official installation guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html). You'll need to have Python 3 installed. Only use `pip` to install Airflow as the other many ways the Python community has come up with to install packages can cause issues, including Poetry and pip-tools. 

Create a temporary constraint file called `constraint.sh`:

```bash
AIRFLOW_VERSION=2.7.1

# Extract the version of Python you have installed. If you're currently using Python 3.11 you may want to set this manually as noted above, Python 3.11 is not yet supported.
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.7.1 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.8.txt
```

Then source it with `source constraint.sh` and install Airflow with `pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"`.

Once completed run the standalone sub-command to populate the database and start all components:

```
airflow standalone
```

Go to the UI at [localhost:8080](http://localhost:8080) and you should see the Airflow UI.

### Docker Compose

For Apache Airflow 2.7.1 you can fetch a pre-made `docker-compose.yaml` file from the documentation:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.1/docker-compose.yaml'
```

Change the version if you want to use something different. The Docker compose method is meant to have an all-in-one setup for development and testing and it isn't recommended for production environments.

Initialize the database before starting the rest of the containers, this is required as it will otherwise not setup the environment correctly including populating the database with its initial data:

```bash
docker compose up airflow-init
```

Then start the rest of the containers with:

```
docker compose up
```

Access the environment at [localhost:8080](http://localhost:8080). Use the default credentials `airflow` and `airflow` to login.

## Lesson 2: Apache Airflow Fundamentals

Airflow has several components that are useful to understand before diving into the code. Start by exploring the simple example to add a Python task to a DAG. Run the task and explore the logs and the UI.

* [Simple DAG](./examples/3-simple/)

## Lesson 3: Creating and running a Pipeline

Creating a pipeline in Airflow allows you to feel more comfortable with core concepts related to Data Engineering. In this example we will create a pipeline that will download a file from the internet, we will clean the dataset using Pandas and then we will persist specific data to a database. All of these actions will be performed in separate steps in tasks.

* [Example pipeline](./examples/4-applied/)

## Lesson 4: Practice Lab

Use the [included practice lab](./lab.md) to build a data pipeline using Apache Airflow to extract census data, transform it, and load it into a database based on certain conditions. Follow the steps in the lab to complete the exercise in your own repository. 

