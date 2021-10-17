from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from uuid import uuid4

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.repository import NamespacesdOligotypeRepository

from .namespace import Namespace
from .oligotype import Oligotype


@dataclass
class NamespacesdOligotype:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    oligotype: Oligotype
    namespace: Namespace
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, namespaced_oligotype_repository: "NamespacesdOligotypeRepository"):
        return namespaced_oligotype_repository.add(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)
