from typing import Any, Dict, Union

from app.adapters.repositories.accession import AccessionRepositoryManager
from app.domain.entities.accession import Accession


def get_list(term: str) -> None:

    response = AccessionRepositoryManager().list_records(term)
    print(response)


def create_accession(payload: Dict[str, Any]) -> Union[bool, Accession]:

    accession = Accession(**payload)
    accession_repo = AccessionRepositoryManager()
    return accession.save(accession_repo)
