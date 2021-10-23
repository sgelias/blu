from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List
from uuid import uuid4

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from ..repository import (
        BlastConfigRepository,
        BlastHitsRepository,
        BlastHspsRepository,
        BlastResultsRepository,
    )

from .accession import Accession
from .oligotype import Oligotype


@dataclass
class BlastConfig:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    program: str
    search_target: Dict[str, str] = field(default_factory=lambda: dict())
    expect: int = field(default=None)
    sc_match: int = field(default=None)
    sc_mismatch: int = field(default=None)
    gap_open: int = field(default=None)
    gap_extend: int = field(default=None)
    filter: str = field(default=None)
    entrez_query: str = field(default=None)
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, blast_config_repository: "BlastConfigRepository"):
        return blast_config_repository.get_or_create(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)


@dataclass
class BlastHsps:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    bit_score: float
    score: int
    evalue: int
    identity: int
    query_from: int
    query_to: int
    query_strand: str
    hit_from: int
    hit_to: int
    hit_strand: str
    align_len: int
    gaps: int
    qseq: str
    hseq: str
    midline: str
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, blast_hsps_repository: "BlastHspsRepository"):
        return blast_hsps_repository.get_or_create(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)


@dataclass
class BlastHits:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    description: List[Accession]
    hsps: List[BlastHsps]
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, blast_hits_repository: "BlastHitsRepository"):
        return blast_hits_repository.get_or_create(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)


@dataclass
class BlastResults:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    blast_config: BlastConfig
    query_oligotype: Oligotype
    search_hits: List[BlastHits]
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, blast_results_repository: "BlastResultsRepository"):
        return blast_results_repository.get_or_create(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)
