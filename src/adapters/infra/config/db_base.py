from typing import Any, Dict

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import scoped_session, sessionmaker

from .db_config import DBConnectionHander

engine = DBConnectionHander().get_engine()
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


# Base = declarative_base()


@as_declarative()
class Base:
    """A declarative base model for database management."""

    # This attributes is necessary for mypy checks.
    query: Any
    metadata: Any

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def as_dict(self) -> Dict[str, Any]:
        """Convert a single database output to dict.

        Returns:
            Dict[str, Any]: The output dictionary.
        """

        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


Base.query = db_session.query_property()
