from typing import List

from app.adapters.infra.config import DBConnectionHander

from app.adapters.infra.entities import AccessionsModel
from app.domain.entities.accession import Accession
from app.domain.repository.accession import AccessionRepository


class DatabaseAccessionRepository(AccessionRepository):
    def add(self, accession: Accession) -> Accession:

        with DBConnectionHander() as conn:
            try:
                accession = AccessionsModel(**accession.__dict__)
                conn.session.add(accession)
                conn.session.commit()
                return accession
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()

    def show(self, term: str) -> List[Accession]:

        # return (
        #     AccessionModel.select()
        #     .where(AccessionModel.accession.contains(term))
        #     .order_by(AccessionModel.accession)
        #     .dicts()
        # )

        return term
