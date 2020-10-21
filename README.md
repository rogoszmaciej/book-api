# book-api

##Installation
Open console in the project root directory. `Docker` and `docker-compose` must be installed.
1. `$ cp .env.example .env`
2. `$ docker-compose build`
3. `$ docker-compose up`
## Load data to the system
Firstly ensure the containers are running

`$ docker ps`

Open shell in container running Django application

`$ docker-compose exec django sh`

Load data with authors details

`$ ./manage.py loadusersdata`

Load books data

`$ ./manage.py loadbooksdata`

Load reviews data

`$ ./manage.py loadreviewsdata`

*[OPTIONAL]* Create custom superuser to access admin area

`$ ./manage.py createsuperuser`

## Tests


**NOTE:** Order in hich the data is loaded is IMPORTANT!
Firstly ensure the containers are running

`$ docker ps`

Execute pytest

`$ docker-compose exec django pytest`
