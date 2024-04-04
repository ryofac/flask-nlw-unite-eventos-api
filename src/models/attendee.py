from sqlalchemy import Column, DateTime, ForeignKey, String, false, func

from src.settings.base import Base


class Attendee(Base):
    __tablename__ = "attendee"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=false)
    email = Column(String, nullable=False)

    # Assim que se relaciona as tabelas:
    event_id = Column(String, ForeignKey("event.id"))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Attendee [id ={self.id}, name={self.name}, event_id={self.event_id}]"
