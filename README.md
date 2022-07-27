# flask-enhanced-template

> Containerized postgres database and flask app using docker-compose

## flask commands

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

Update and Downgrade database

```commandline
flask db upgrade
flask db downgrade
```
