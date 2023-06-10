import os

from flask_migrate import Migrate

from app import create_app, db
from app.models import *

app = create_app(os.getenv("ENVIRONMENT", "DEVELOPMENT"))
migrate = Migrate(app, db)


@app.cli.command("setup-database")
def setup_db():
    try:
        db.drop_all()
        print("Setting up database...")
        db.create_all()
        print("Database setup successfully")
    except Exception as e:
        print("Failed to setup database")
        print(str(e))
