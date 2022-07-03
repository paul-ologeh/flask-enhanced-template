import uuid
from datetime import datetime
from app import db
from sqlalchemy.dialects.postgresql import UUID


class Health(db.Model):
    __tablename__ = "health_checks"
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    message = db.Column(db.Text(), default="Ok")
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)
