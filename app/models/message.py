# ./app/models/message.py

from .base import BaseModel, db


class Message(BaseModel):
    __tablename__ = 'messages'

    sender_id = db.Column(
        db.String(60), db.ForeignKey('users.id'), nullable=False)
    message_body = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Message (ID: {self.id}, Sender ID: {self.sender_id})>"
