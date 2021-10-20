from abc import ABCMeta, abstractmethod
from typing import List

from src.domain.entities import Accession


class AccessionRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, accession: Accession) -> Accession:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Accession]:
        raise NotImplementedError
