from flask import Blueprint
from app.models import health
from app import db

api_v1 = Blueprint("v1", __name__, url_prefix="/v1")


@api_v1.route("/health", methods=["GET"])
def health_check():
    health_entry = health()
    db.session.add(health_entry)
    db.session.commit()

    return "Ok"
