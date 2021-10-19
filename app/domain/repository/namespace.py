from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from app.domain.entities import Namespace


class NamespaceRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, namespace: Namespace) -> Tuple[bool, Namespace]:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Namespace]:
        raise NotImplementedError

    @abstractmethod
    def edit(self) -> Namespace:
        raise NotImplementedError
