from uuid import uuid4

from src.adapters.infra.config import Base
from sqlalchemy import Column, String, Text


class NamespacesModel(Base):
    """Namespaces entity."""

    __tablename__ = "blu_namespaces"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)

    namespace = Column(String(100), nullable=False, unique=True)

    def __repr__(self) -> str:
        return self.namespace
