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
