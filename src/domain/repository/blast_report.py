from abc import ABCMeta, abstractmethod

from src.domain.entities import BlastConfig, BlastHits, BlastHsps, BlastResults


class BlastConfigRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, blast_config: BlastConfig) -> BlastConfig:
        raise NotImplementedError

    @abstractmethod
    def get(self) -> BlastConfig:
        raise NotImplementedError


class BlastHspsRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, blast_hsps: BlastHsps) -> BlastHsps:
        raise NotImplementedError

    @abstractmethod
    def get(self) -> BlastHsps:
        raise NotImplementedError


class BlastHitsRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, blast_hits: BlastHits) -> BlastHits:
        raise NotImplementedError

    @abstractmethod
    def get(self) -> BlastHits:
        raise NotImplementedError


class BlastResultsRepository(metaclass=ABCMeta):

    # -------------------------------------------------------------------------
    # ABSTRACT METHODS
    # -------------------------------------------------------------------------

    @abstractmethod
    def add(self, blast_results: BlastResults) -> BlastResults:
        raise NotImplementedError

    @abstractmethod
    def get(self) -> BlastResults:
        raise NotImplementedError
