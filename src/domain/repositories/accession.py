from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from src.domain.data_stores import Accession


class AccessionRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_or_create(self, accession: Accession) -> Tuple[bool, Accession]:
        raise NotImplementedError

    @abstractmethod
    def show(self, term: str) -> List[Accession]:
        raise NotImplementedError
