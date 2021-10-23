from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from src.domain.data_stores import Oligotype


class OligotypeRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_or_create(self, oligotype: Oligotype) -> Tuple[bool, Oligotype]:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Oligotype]:
        raise NotImplementedError

    @abstractmethod
    def edit(self) -> Oligotype:
        raise NotImplementedError
