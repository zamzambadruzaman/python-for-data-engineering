## **Workshop Python for Data Engineering**

**Setup MyQSL Database :**
- docker pull mysql:5.7
- docker run   --publish=3306:3306 --name local-mysql -e MYSQL_ROOT_PASSWORD=password123 -d mysql:5.7


**Setup Python**
- install python 3, download disini : https://www.python.org/downloads/
- Ikuti langkah-langkah instalasi, dan pastikan python 3 terinstall di komputer masing-masing
- buat Virtual environment : python -m venv ./venv

**PySpark**
- install PySpark => pip install pyspark

**Great Expectations**
- pip install great_expectations

**Airflow**
```
export AIRFLOW_HOME=~/airflow
AIRFLOW_VERSION=2.1.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

initialize the database

`airflow db init`

create aifrflow user
``` 
airflow users create \
    --username admin \
    --firstname admin \
    --lastname idbigdata \
    --role Admin \
    --email admin@idbigdata.com
```
start the web server, default port is 8080
`airflow webserver --port 8080`

start the scheduler
open a new terminal or else run webserver with ``-D`` option to run it as a daemon

`airflow scheduler`
