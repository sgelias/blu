from uuid import uuid4

from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import relationship
from src.adapters.infra.config import Base


class OligotypesModel(Base):
    """Oligotypes entity."""

    __tablename__ = "blu_oligotypes"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)

    oligotype = Column(String(15), nullable=False, unique=True)
    oligotype_code = Column(Integer, nullable=True)
    is_default_oligotype = Column(Boolean, nullable=False)
    blast_results = relationship("BlastResultsModel")

    def __repr__(self) -> str:
        return self.oligotype
