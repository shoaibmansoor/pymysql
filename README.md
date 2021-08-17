# pymysql
MySql CRUD modules in python

We need 2 env variables with appropriate values: DB_USERNAME;DB_PASSWORD;

### Create a virtual env
`virtualenv -p python3 venv`

### Activate the virtual env
`.\venv\Scripts\activate`

### Install dependencies
`pip install -r requirement.txt`

### Create DB and tables with MySQL Alchemy
Takes configutation from 'config.py'. Execute following commands:
```
$ python3 migrate.py db init
$ python3 migrate.py db migrate
$ python3 migrate.py db upgrade
```

### Start the application
`$ python run.py`


#### Basic MySql Examples
`$ python mysql_basic_crud_examples.py`