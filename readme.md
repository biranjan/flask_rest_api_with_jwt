## Start the DB
`docker-compose up --build`
- make user all the environment variables are set-up

## Migrate the database

`python manage.py db int`

`python manage.py db migrate`

`python manage.py db upgrade`

## Run the app

`python3 run.py`