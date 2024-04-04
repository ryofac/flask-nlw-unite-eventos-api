from sqlalchemy import Column, Integer, String

from src.settings.base import Base  # Importando a base configurada só no brilho

""" Classe que irá abstrair a lógica de evento na aplicação """


class Event(Base):
    __tablename__ = "event"
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer)

    def __repr__(self):
        return (
            f"Event [title={self.title}. maximum_atendees=[{self.maximum_attendees}]]"
        )
