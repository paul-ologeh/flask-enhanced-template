from flask import Blueprint

from app import db
from app.models import Health

api_v1 = Blueprint("v1", __name__, url_prefix="/v1")


@api_v1.route("/health", methods=["GET"])
def health_check():
    health_entry = Health(api_version=1)
    db.session.add(health_entry)
    db.session.commit()

    return "Ok"
