from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class __DBConnectionHandler:

    _db_used = "sqlite"
    _db_file = "storage.db"

    def __init__(self) -> None:
        self.__connection_string = f"{self._db_used}:///{self._db_file}"
        # Definido posteriormente:
        self.session = None
        self.__engine = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    # Métodos para a utilização como contexto:
    def __enter__(self):
        session_maker = sessionmaker()
        # Definindo uma sessão para a operanção com o banco:
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, *args, **kwargs):
        self.session.close()


# Fazendo com que o DBConnectionHAndler tenha só uma instância
# "Estático"
db_connection_handler = __DBConnectionHandler()
