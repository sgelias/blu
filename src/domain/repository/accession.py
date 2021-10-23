from abc import ABCMeta, abstractmethod
from typing import List

from src.domain.data_stores import Accession


class AccessionRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_or_create(self, accession: Accession) -> Accession:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Accession]:
        raise NotImplementedError
