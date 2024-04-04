import pytest

from src.repository.attendee_repository import AttendeeRepository
from src.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip("Teste já realizado")
def test_atendee_creation():
    atendee_info = {
        "id": "asdds21a",
        "name": "Roberto Carlos",
        "email": "robertocarlos@gmail.com",
        "event_id": "uhu-eh-nois-na-pista",
    }
    atendee_repository = AttendeeRepository()
    response = atendee_repository.insert_atendee(atendee_info=atendee_info)
    print(response)


def test_get_attendee_badge_by_id():
    attendee_repository = AttendeeRepository()
    attendee_id = "asddsa"
    response = attendee_repository.get_attendee_badge_by_id(attendee_id)
    print(response)
