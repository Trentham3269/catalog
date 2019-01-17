# Catalog App

A web application to list items based on their category. Requires sign in with Google authentication/authorisation to edit, create and delete items. 

## Dependencies
### System
This code requires the following to run:
+ [Linux](https://www.linux.org/)
+ [Python 3](https://www.python.org/downloads/)
+ [PostgreSQL](https://www.postgresql.org/)

### Python Libraries
Install these python libraries by running `$ pip3 install -r requirements.txt`:
+ [flask](http://flask.pocoo.org/)
+ [sqlalchemy](https://www.sqlalchemy.org/)
+ [oauth2client](https://github.com/googleapis/oauth2client)
+ [psycopg2](http://initd.org/psycopg/)
+ [requests](http://docs.python-requests.org/en/master/)

### OAuth 2.0
OAuth 2.0 is implemented in this application with the [Google API Client for Python](https://developers.google.com/api-client-library/python/guide/aaa_oauth) so you will require a ```client_secrets.json``` file in the root ('/') directory of this repo. 

I have not included my ```client_secrets.json``` as Google's documentation states **Warning:** *Keep your client secret private. If someone obtains your client secret, they could use it to consume your quota, incur charges against your Google APIs Console project, and request access to user data.* 

You will therefore need to setup and download your own OAuth 2.0 client ID for this application in Google's [Developer Console](https://console.developers.google.com) with the following configuration:
+ Application type: Web application
+ Name: Catalog App
+ Authorized JavaScript origins: http://localhost:8000
+ Authorized redirect URIs: http://localhost:8000/login **and** http://localhost:8000/gconnect
 
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

![App Screenshot](./img/app.png?raw=true)

The application also provides an endpoint at http://localhost:8000/catalog/api which returns JSON like this:

![API Screenshot](./img/api.png?raw=true)

## Style Guide
The [Pep8](https://www.python.org/dev/peps/pep-0008/) style guide is used. You can install [pycodestyle](https://pypi.org/project/pycodestyle/) on Linux with `$ pip3 install pyscodestyle` and then run `$ pycodestyle app.py` to check the code's adherence to the standard. 
