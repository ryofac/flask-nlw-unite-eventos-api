import pytest

from src.repository.event_repository import EventRepository
from src.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Teste já realizado, dado já presente no banco")
def test_event_creation():
    test_event = {
        "id": "uhu-eh-nois-na-pista",
        "title": "titlezinho massa",
        "slug": "meu-slug",
    }
    event_repository = EventRepository()
    event_created = event_repository.insert_event(test_event)
    print(event_created)


def test_get_event_by_id():
    event_repository = EventRepository()
    event_id = "uhu-eh-nois-na-pista"
    response = event_repository.get_event_by_id(event_id=event_id)
    print(response)
