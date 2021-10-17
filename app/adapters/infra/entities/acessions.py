from uuid import uuid4

from app.adapters.infra.config import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .blastn_report import blast_hits_accessions


class AccessionsModel(Base):
    """Accessions entity."""

    __tablename__ = "nop_accessions"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)

    accession = Column(String(15), nullable=False, unique=True)
    title = Column(String)
    taxid = Column(Integer, nullable=True)
    sciname = Column(String)
    sciname_clean = Column(String)
    blast_hits = relationship(
        "BlastHitsModel", back_populates="description", secondary=blast_hits_accessions
    )

    def __repr__(self) -> str:
        return self.accession
