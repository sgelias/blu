from abc import ABCMeta, abstractmethod
from typing import List

from app.domain.entities.accession import Accession


class AccessionRepository(metaclass=ABCMeta):
    @abstractmethod
    def add(self, accession: Accession) -> Accession:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> List[Accession]:
        raise NotImplementedError
