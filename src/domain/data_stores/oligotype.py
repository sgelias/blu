from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional
from uuid import uuid4

if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from ..repository import OligotypeRepository


@dataclass
class Oligotype:

    # -------------------------------------------------------------------------
    # FIELD DEFINITIONS
    # -------------------------------------------------------------------------

    oligotype: str
    oligotype_code: Optional[int] = field(default=None)
    is_default_oligotype: bool = field(default_factory=lambda: False)
    id: str = field(default_factory=lambda: str(uuid4()))

    # -------------------------------------------------------------------------
    # PUBLIC METHODS
    # -------------------------------------------------------------------------

    def save(self, oligotype_repository: "OligotypeRepository"):

        self.__check_and_initialize_default_oligotype()
        return oligotype_repository.get_or_create(self)

    # -------------------------------------------------------------------------
    # MAGIC METHODS
    # -------------------------------------------------------------------------

    def __hash__(self):
        return hash(self.id)

    # -------------------------------------------------------------------------
    # PRIVATE METHODS
    # -------------------------------------------------------------------------

    def __check_and_initialize_default_oligotype(self) -> None:
        """Check if oligotype is default.

        Returns:
            bool: True if oligotype see the default format. False otherwise.
        """

        oligotype = self.oligotype.split("_")

        if len(oligotype) == 3:
            if all(
                [
                    self.__could_be_integer(oligotype[1]),
                    self.__could_be_integer(oligotype[2]),
                ]
            ):
                self.is_default_oligotype = True
                self.oligotype_code = int(oligotype[1])

    @staticmethod
    def __could_be_integer(value: Any) -> bool:
        """Verify if provided value could be converted to a integer.

        Args:
            value (Any): [description]

        Returns:
            bool: True if value could be converted to a integer. False
            otherwise.
        """

        try:
            int(value)
            return True
        except:
            return False
