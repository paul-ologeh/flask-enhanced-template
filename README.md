# flask-enhanced-template

> Containerized postgres database and flask app using docker-compose

# Setup

Run containers using docker-compose

```commandline
docker-compose -f docker-compose.yml up -d
```

Setup database schema by running the following command inside the flask container

```commandline
flask setup-database
```

# Testing

Create the test database inside the postgres container

```commandline
docker exec -it <container-id> /bin/bash
psql -U postgres
CREATE DATABASE "flask-enhanced-test";
```

Run the following command inside the flask container to run the tests

```commandline
python run_tests.py
```

# Additional Information

- See flask.log for flask logs
- Database is forwarded to port 8001
- Flask app is forwarded to port 8000

## common flask commands

Initialise schema

```commandline
flask setup-database
```

Setup migrations

```commandline
flask db init
```

Create migration

```commandline
flask db migrate -m "migration message"
```

Run tests

```commandline
flask test
```

Do and Undo database migration

```commandline
flask db upgrade
flask db downgrade
```
