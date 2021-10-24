from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from src.domain.data_stores import NamespacedOligotype


class NamespacedOligotypeRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_or_create(
        self, namespaced_oligotype: NamespacedOligotype
    ) -> Tuple[bool, NamespacedOligotype]:
        raise NotImplementedError

    @abstractmethod
    def show(self, term: str) -> List[NamespacedOligotype]:
        raise NotImplementedError
