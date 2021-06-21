## **idBIgData Workshop : Python for Data Engineering**

**Clone or Download this Repository**

If you have `git` installed in your machine :

`git clone https://github.com/zamzambadruzaman/python-for-data-engineering.git`

Clone the repo without git :
- Download the repo : [Download zip](https://github.com/zamzambadruzaman/python-for-data-engineering/archive/refs/heads/master.zip)
- Extract the zip

**Setup Python**
- install python 3.7.x or above, download [here](https://www.python.org/downloads/)
- Follow the installation, and make sure python 3 successfully is installed in your machine :
  
  `python3 --version`
- go to the repository directory and create a virtual environment :
  
  `python3 -m venv ./venv`
  
**Install Python IDE**

You can use your favorite IDE :
- [PyCharm](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu)
- [Visual Code](https://code.visualstudio.com/Download)
- [Spyder](https://docs.spyder-ide.org/current/installation.html)
- [Vim](https://www.vim.org/download.php)
- etc

**Setup MyQSL Database :**

In this workshop we will use MySQL 5.7 or above.
There are two options to install the database server :
Options 1 : Local server or VM :
- Download the installation package :
  - Windows : [Download](https://dev.mysql.com/downloads/file/?id=502540)
  - Linux : [Download](https://dev.mysql.com/downloads/file/?id=502515)
  - MacOS : [Download](https://dev.mysql.com/downloads/file/?id=505134)
- Double click teh installer and follow the installation instruction

Options 2 : Install with Docker :
- docker pull mysql:5.7
- docker run   --publish=3306:3306 --name local-mysql -e MYSQL_ROOT_PASSWORD=password123 -d mysql:5.7

Install MySQL Workbench (or your favorite MySQL Client) :
- Download the installer : [Download](https://dev.mysql.com/downloads/workbench/)
- Double click the installer and follow the instruction.

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

create airflow user
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
