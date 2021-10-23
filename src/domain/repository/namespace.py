from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from src.domain.data_stores import Namespace


class NamespaceRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_or_create(self, namespace: Namespace) -> Tuple[bool, Namespace]:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Namespace]:
        raise NotImplementedError

    @abstractmethod
    def edit(self) -> Namespace:
        raise NotImplementedError
