from sqlalchemy import Column, DateTime, ForeignKey, String, func

from src.settings.base import Base


class CheckIn(Base):
    __tablename__ = "check_in"
    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendee_id = Column(String, ForeignKey("attendee.id"))

    def __repr__(self):
        return f"CheckIn [id ={self.id}, attendee_if={self.attendee_id}]"
