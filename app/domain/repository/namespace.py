from abc import ABCMeta, abstractmethod
from typing import List

from app.domain.entities import Namespace


class NamespaceRepository(metaclass=ABCMeta):
    @abstractmethod
    def add(self, namespace: Namespace) -> Namespace:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Namespace]:
        raise NotImplementedError
