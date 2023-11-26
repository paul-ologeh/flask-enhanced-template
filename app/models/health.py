import uuid
from datetime import datetime

from flask_sqlalchemy.model import DefaultMeta
from sqlalchemy.dialects.postgresql import UUID

from app import db

BaseModel: DefaultMeta = db.Model


class Health(BaseModel):
    __tablename__ = "health_checks"
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    message = db.Column(db.Text(), default="Ok")
    api_version = db.Column(db.Integer(), nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)
