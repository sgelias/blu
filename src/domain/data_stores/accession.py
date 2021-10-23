from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional
from uuid import uuid4

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from ..repository import AccessionRepository


@dataclass
class Accession:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    accession: str
    title: str
    taxid: Optional[int]
    sciname: Optional[str]
    sciname_clean: Optional[str]
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC
    # -------------------------------------------------------------------------

    def save(self, accession_repository: "AccessionRepository"):
        return accession_repository.get_or_create(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)
