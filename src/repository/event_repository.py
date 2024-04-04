from ast import Dict

from sqlalchemy.exc import IntegrityError

from src.models.event import Event
from src.settings.connection import db_connection_handler


class EventRepository:
    def insert_event(self, event_info: Dict):
        try:
            with db_connection_handler as db:
                # Coletando os dados do dicionário no momento da insersão do evento
                event = Event(
                    id=event_info.get("id"),
                    title=event_info.get("title"),
                    details=event_info.get("details"),
                    slug=event_info.get("slug"),
                    maximum_attendees=event_info.get("maximum_attendees"),
                )
                # Adcionando o model no db
                db.session.add(event)

                # Salvando a migration
                db.session.commit()

                return event_info
        except IntegrityError:
            raise Exception("Erro: Transação inconsistente")

        except Exception as ex:
            # Qualquer exceção gera um rollback no bd
            db.session.rollback()
            raise ex

    def get_event_by_id(self, event_id: str) -> Event:
        with db_connection_handler as db:
            event = db.session.query(Event).filter(Event.id == event_id).one_or_none()
            return event
