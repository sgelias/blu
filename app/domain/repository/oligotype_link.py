from abc import ABCMeta, abstractmethod
from typing import List

from app.domain.entities import Oligotype, Namespace, NamespacesdOligotype


class NamespacesdOligotypeRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, oligotype: Oligotype, namespace: Namespace) -> NamespacesdOligotype:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[NamespacesdOligotype]:
        raise NotImplementedError
