from app.settings import SQLITE_DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHander:
    """Sqlalchemy datbase connection class."""

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __init__(self) -> None:

        self.__connection_string = f"sqlite:///{SQLITE_DATABASE}"
        self.session = None

    def __enter__(self):

        eng = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=eng)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.session.close_all()

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def get_engine(self):
        """Provide the database connection engine."""

        return create_engine(self.__connection_string)
