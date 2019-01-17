# Catalog

A web application to list items based on their category. Requires sign in with Google authentication/authorisation to edit, create and delete items. 

## Dependencies
This code requires the following to run:
+ [Linux](https://www.linux.org/)
+ [Python 3](https://www.python.org/downloads/)
+ [PostgreSQL](https://www.postgresql.org/)

Install these python libraries by running `pip3 install -r requirements.txt`:
+ [flask](http://flask.pocoo.org/)
+ [sqlalchemy](https://www.sqlalchemy.org/)
+ [oauth2client](https://github.com/googleapis/oauth2client)
+ [psycopg2](http://initd.org/psycopg/)
+ [requests](http://docs.python-requests.org/en/master/)
 
## Database
### Setup
To setup the database run `$ psql catalog < data/db_setup.sql`

### Structure
The database includes two tables:
+ The categories table includes each sport category `\d categories`
+ The items table includes the items and their descriptions `\d items`

## Application
To run the application:
```
$ git clone https://github.com/Trentham3269/catalog.git && cd catalog
$ git checkout fix
$ ./app.py

```
You can then view the application in a web browser at http://localhost:8000. It should look something like this:

![App Screenshot](./app.png?raw=true)

## Style Guide
The [Pep8](https://www.python.org/dev/peps/pep-0008/) style guide is used. You can install [pycodestyle](https://pypi.org/project/pycodestyle/) on Linux with `$ pip3 install pyscodestyle` and then run `$ pycodestyle app.py` to check the code's adherence to the standard. 

