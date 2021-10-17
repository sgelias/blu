from typing import List

from app.adapters.infra.config import DBConnectionHander
from app.adapters.infra.entities import AccessionsModel
from app.domain.entities import Accession
from app.domain.repository import AccessionRepository
from dacite import from_dict


class AccessionRepositoryManager(AccessionRepository):
    """A manager of Accessions model."""

    @staticmethod
    def add(accession: Accession) -> Accession:
        """Insert a single record into database

        Args:
            accession (Accession): An acession object.

        Returns:
            Accession: A instance of the created accession.
        """

        with DBConnectionHander() as conn:
            try:
                accession = AccessionsModel(**accession.__dict__)
                conn.session.add(accession)
                conn.session.commit()

                return Accession(
                    id=accession.id,
                    accession=accession.accession,
                    title=accession.title,
                    taxid=accession.taxid,
                    sciname=accession.sciname,
                    sciname_clean=accession.sciname_clean,
                )

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
