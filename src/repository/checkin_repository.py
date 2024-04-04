from sqlite3 import IntegrityError
from typing import Dict

from src.settings.connection import db_connection_handler


class CheckInRepository:
    def insert_check_in(self, check_in_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                db.session.add(
                    id=check_in_info.get("id"),
                    created_at=check_in_info.get("created_at"),
                    attendee_id=check_in_info.get("attendee_id"),
                )

                return check_in_info

            except IntegrityError:
                raise Exception("Erro: Transação inconsistente")
            except Exception as ex:
                db.session.rollback()
                raise ex
