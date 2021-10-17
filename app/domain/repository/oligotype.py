from abc import ABCMeta, abstractmethod
from typing import List

from app.domain.entities import Oligotype


class OligotypeRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, oligotype: Oligotype) -> Oligotype:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Oligotype]:
        raise NotImplementedError

    @abstractmethod
    def edit(self) -> Oligotype:
        raise NotImplementedError
