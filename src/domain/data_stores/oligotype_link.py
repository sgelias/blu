from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from uuid import uuid4

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from ..repository import NamespacedOligotypeRepository

from .namespace import Namespace
from .oligotype import Oligotype


@dataclass
class NamespacedOligotype:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    oligotype: Oligotype
    namespace: Namespace
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, namespaced_oligotype_repository: "NamespacedOligotypeRepository"):
        return namespaced_oligotype_repository.get_or_create(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)
