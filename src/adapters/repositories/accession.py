from typing import List, Tuple

from src.adapters.infra.config import DBConnectionHander
from src.adapters.infra.entities import AccessionsModel
from src.domain.data_stores import Accession
from src.domain.repository import AccessionRepository
from dacite import from_dict


class AccessionRepositoryManager(AccessionRepository):
    """A manager of Accessions model."""

    @staticmethod
    def get_or_create(accession: Accession) -> Tuple[bool, Accession]:
        """Insert a single record into database

        Args:
            accession (Accession): An acession object.

        Returns:
            Tuple[bool, Accession]: A boolean indicating if the accession was
            created (True) or recovered from database (False), and a instance
            of the created accession.
        """

        old_accession = AccessionsModel.query.filter(
            AccessionsModel.accession == accession.accession
        ).first()

        if old_accession:
            return False, from_dict(Accession, old_accession.as_dict())

        with DBConnectionHander() as conn:
            try:
                new_accession = AccessionsModel(**accession.__dict__)
                conn.session.add(new_accession)
                conn.session.commit()
                return True, from_dict(Accession, new_accession.as_dict())

            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()

    @staticmethod
    def show(term: str) -> List[Accession]:
        """List accessions given the search term.

        Args:
            term (str): A term to filter accessions.

        Returns:
            List[Accession]: A list of filtered accessions.
        """

        if term:
            return [
                from_dict(Accession, record.__dict__)
                for record in (
                    AccessionsModel.query.filter(
                        AccessionsModel.accession == term
                    ).order_by(AccessionsModel.accession.desc())
                )
            ]

        return [
            from_dict(Accession, record.__dict__)
            for record in (
                AccessionsModel.query.order_by(AccessionsModel.accession.desc())
            )
        ]
