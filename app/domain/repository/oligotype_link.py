from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from app.domain.entities import NamespacedOligotype


class NamespacedOligotypeRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(
        self, namespaced_oligotype: NamespacedOligotype
    ) -> Tuple[bool, NamespacedOligotype]:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[NamespacedOligotype]:
        raise NotImplementedError
