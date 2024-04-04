from sqlite3 import IntegrityError
from typing import Dict

from src.entities.attendee import Attendee
from src.entities.event import Event
from src.settings.connection import db_connection_handler


class AttendeeRepository:
    def insert_atendee(self, atendee_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                attendee = Attendee(
                    id=atendee_info.get("id"),
                    name=atendee_info.get("name"),
                    email=atendee_info.get("email"),
                    event_id=atendee_info.get("event_id"),
                    created_at=atendee_info.get("created_at"),
                )
                db.session.add(attendee)
                db.session.commit()

                return atendee_info

            except IntegrityError:
                raise Exception("Erro: Transação inconsistente")
            except Exception as ex:
                db.session.rollback()
                raise ex

    def get_attendee_badge_by_id(self, attendee_id: str):
        with db_connection_handler as db:
            attendee_badge = (
                db.session.query(Attendee)
                .join(Event, Event.id == Attendee.event_id)
                .filter(Attendee.id == attendee_id)
                .with_entities(
                    Attendee.name,
                    Attendee.email,
                    Event.title,
                )
                .one_or_none()
            )
            return attendee_badge
