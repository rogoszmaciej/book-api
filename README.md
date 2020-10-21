# book-api

## Installation
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

**NOTE:** Order in which the data is loaded is IMPORTANT!

## Tests
Firstly ensure the containers are running

`$ docker ps`

Execute pytest

`$ docker-compose exec django pytest`

## Available endpoint

### Books
1. GET `/books/list/` - list all books (without reviews)
2. GET `/books/details/<pk>` - get book details by book ID (with related reviews)
3. GET `/books/search/<search_phrase>` - get books by `search_phrase` (with related reviews)

###Reviews
1. GET `reviews/book_reviews/<book_pk>` - get reviews by book ID
2. GET `reviews/details/<pk>` - get review details by review ID
