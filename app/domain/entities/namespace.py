from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from uuid import uuid4

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.repository import NamespaceRepository


@dataclass
class Namespace:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    namespace: str
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, namespace_repository: "NamespaceRepository"):
        return namespace_repository.add(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)
