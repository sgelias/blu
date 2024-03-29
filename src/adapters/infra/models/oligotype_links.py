from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Text
from src.adapters.infra.config import Base


class NamespacedOligotypesModel(Base):
    """NamespacedOligotypes entity."""

    __tablename__ = "blu_namespaced_oligotypes"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)

    oligotype = Column(Text, ForeignKey("blu_oligotypes.id"))
    namespace = Column(Text, ForeignKey("blu_namespaces.id"))

    def __repr__(self) -> str:
        return f"{self.oligotype} | {self.namespace}"
