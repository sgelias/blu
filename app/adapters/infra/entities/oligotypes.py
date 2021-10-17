from uuid import uuid4

from app.adapters.infra.config import Base
from sqlalchemy import Column, String, Text, Boolean, Integer
from sqlalchemy.orm import relationship


class OligotypesModel(Base):
    """Oligotypes entity."""

    __tablename__ = "nop_oligotypes"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)

    oligotype = Column(String(15), nullable=False, unique=True)
    oligotype_code = Column(Integer, nullable=True)
    is_default_oligotype = Column(Boolean, nullable=False)
    blast_results = relationship("BlastResultsModel")

    def __repr__(self) -> str:
        return self.oligotype
