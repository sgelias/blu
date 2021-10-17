from abc import ABCMeta, abstractmethod
from typing import List

from app.domain.entities.accession import Accession


class AccessionRepository(metaclass=ABCMeta):
    @abstractmethod
    def add_accession(self, accession: Accession) -> Accession:
        raise NotImplementedError

    @abstractmethod
    def list_records(self) -> List[Accession]:
        raise NotImplementedError
