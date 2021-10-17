from typing import List

from app.adapters.database.accessions_model import AccessionModel
from app.domain.entities.accession import Accession
from app.domain.repository.accession import AccessionRepository


class DatabaseAccessionRepository(AccessionRepository):
    def add(self, accession: Accession) -> Accession:

        accession, _ = AccessionModel.get_or_create(
            accession=accession.accession, defaults={**accession.__dict__}
        )

        return accession

    def show(self, term: str) -> List[Accession]:

        return (
            AccessionModel.select()
            .where(AccessionModel.accession.contains(term))
            .order_by(AccessionModel.accession)
            .dicts()
        )
