## Using venv 

Pipenv instead of pip -venv

## Usage of PyCharm

Adding the source folder.

## Peculiarity of python

Pep8

Usage of `if __name__ == '__main__':`

The help of **PYTHONPATH**

## DB

### Sessions

You shouldn't create too many sessions for the DB transactions in 
sqlAqlchemy. Instead create the scoped session and a "closure" to
close the session when the server stops.

### migrations

SQL Alchemy doesn't have migration capabilities, to address it 
a new library was created, called alembic.

To start you need to create the configuration files.

```
$ pipenv shell
(server)$ alembic init alembic
```

In **alembic.ini** set **sqlalchemy.url** to `sqlalchemy.url = sqlite:///src/flaskart.sqlite`


In **alembic/env.py** replace **target_metadata = None** with

```
from src.connections.db.base_model import DbBase
import api.products.models
target_metadata = DbBase.metadata
```

It's important to add the model classes to *env* file

And in the console 

```
(server)$ PYTHONPATH=/Users/<user_name>/location/flaskart_rest_course/server/src alembic revision --autogenerate -m 'Added first product table'
```

To generate a new Migration file

```
(server)$ PYTHONPATH=/Users/project/location/flaskart_rest_course/server/ alembic revision -m 'A new change table'
```

To confirm / Commit the migration changes.

`PYTHONPATH=/Users/project/location/flaskart_rest_course/server/ alembic upgrade head`


## Testing. 

Install the test library

`pipenv install pytest`

To run the test cases 

```
$ pipenv shell
(server)$ py.test
```

Autodetect testing works for __test*.py__ or __*test.py__. Ex. *my_model_test.py*

If the import fails remember to set the _WORKDIR_

Helpers:
  - -v to show verbose / detailed output
  - -s to show stdout (print/log) output 

## Content

### Sess 1

* Introduction to python. Core aspects of the language.
* Tools to work with python. IDE's and text editors.
* PEP8
  * Indentation
  * Variables types.
* Virtual environments (Pip, pipenv) (Now going with pip env.)
* Installing packages.
* Flask. Run, basic configurations, basic routing.
  * Imports
  * Setting the IDE to recognize source folders.
  * `if __name__`
* REST
  * Blueprints.
  * Decorators, usage.
  * Registering blueprints.
  * Using the `request` object.
  * Json Responses
* DB
  * SQl, Sql Alchemy
  * Connection with the database.
  * Using first `create_all` method.
  * Creating the session object.
* Python Classes (Model)
  * Classes.
  * Creating the model class.
  * `__repr__` `classmethod`, args & kwargs
  * Using the session object on model operations
* Serializers / Marshmallow.
  * Model Schema.
  * Dump, Load Jsons.
* Migrations / alembic.
  * Creating / running migrations scripts.
  
### Sess 2

* Python testing / Pytest.
  * Testing principles
  * Creating the first test case.
  * Run the test cases.
  * Using fixtures
* Python generators.
  * Factory pattern
  * Flask create_app factory
* CORS
  * Add and install flask-cors
* File uploading
  * Multipart forms.
  * Static folder
  * Storing Files.
    * Importance of file securing.
  * Create the static routing.
  * Create a serializer with a post_dump.
    * Explain serializer post, pre decorator.
    


