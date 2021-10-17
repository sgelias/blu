from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional
from uuid import uuid4

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.repository import AccessionRepository


@dataclass
class Accession:

    accession: str
    title: str
    taxid: Optional[int]
    sciname: Optional[str]
    sciname_clean: Optional[str]
    id: str = field(default_factory=lambda: str(uuid4()))

    def save(self, accession_repository: "AccessionRepository"):
        return accession_repository.add(self)

    def __hash__(self):
        return hash(self.id)
