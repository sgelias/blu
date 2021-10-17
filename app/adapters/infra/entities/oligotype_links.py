from uuid import uuid4

from app.adapters.infra.config import Base
from sqlalchemy import Column, ForeignKey, Text


class NamespacedOligotypesModel(Base):
    """NamespacedOligotypes entity."""

    __tablename__ = "nop_namespaced_oligotypes"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)

    oligotype = Column(Text, ForeignKey("nop_oligotypes.id"))
    namespace = Column(Text, ForeignKey("nop_namespaces.id"))

    def __repr__(self) -> str:
        return f"{self.oligotype} | {self.namespace}"
