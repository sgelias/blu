import json
from uuid import uuid4

from app.adapters.infra.config import Base
from sqlalchemy import (
    Column,
    Date,
    Float,
    ForeignKey,
    Integer,
    Table,
    Text,
    TypeDecorator,
    types,
)
from sqlalchemy.orm import relationship


class Json(TypeDecorator):
    @property
    def python_type(self):
        return object

    impl = types.String

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_literal_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialect):
        try:
            return json.loads(value)
        except (ValueError, TypeError):
            return None


class BlastConfigModel(Base):
    """BlastConfig entity."""

    __tablename__ = "nop_blast_config"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    program = Column(Text(10), nullable=False)
    search_target = Column(Json, nullable=False)
    expect = Column(Integer, nullable=False)
    sc_match = Column(Integer, nullable=False)
    sc_mismatch = Column(Integer, nullable=False)
    gap_open = Column(Integer, nullable=False)
    gap_extend = Column(Integer, nullable=False)
    filter = Column(Text(10), nullable=False)
    entrez_query = Column(Text, nullable=False)
    blast_results = relationship("BlastResultsModel")


class BlastHspsModel(Base):
    """BlastHsps entity."""

    __tablename__ = "nop_blast_hsps"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    bit_score = Column(Float, nullable=False)
    score = Column(Integer, nullable=False)
    evalue = Column(Integer, nullable=False)
    identity = Column(Integer, nullable=False)
    query_from = Column(Integer, nullable=False)
    query_to = Column(Integer, nullable=False)
    query_strand = Column(Text(10), nullable=False)
    hit_from = Column(Integer, nullable=False)
    hit_to = Column(Integer, nullable=False)
    hit_strand = Column(Text(10), nullable=False)
    align_len = Column(Integer, nullable=False)
    gaps = Column(Integer, nullable=False)
    qseq = Column(Text, nullable=False)
    hseq = Column(Text, nullable=False)
    midline = Column(Text, nullable=False)


blast_hits_accessions = Table(
    "nop_blast_hits_accessions",
    Base.metadata,
    Column(
        "nop_blast_hits_id", Text, ForeignKey("nop_blast_hits.id"), primary_key=True
    ),
    Column(
        "nop_accessions_id", Text, ForeignKey("nop_accessions.id"), primary_key=True
    ),
    Column("created_at", Date),
)


class BlastHitsModel(Base):
    """BlastHits entity."""

    __tablename__ = "nop_blast_hits"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    query_oligotype = Column(Text, ForeignKey("nop_blast_results.id"))
    description = relationship(
        "AccessionsModel", back_populates="blast_hits", secondary=blast_hits_accessions
    )


class BlastResultsModel(Base):
    """BlastResults entity."""

    __tablename__ = "nop_blast_results"

    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    blast_config = Column(Text, ForeignKey("nop_blast_config.id"))
    query_oligotype = Column(Text, ForeignKey("nop_oligotypes.id"))
    search_hits = relationship("BlastHitsModel")
