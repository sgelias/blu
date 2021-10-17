from typing import Any, Dict, Union

from app.adapters.managers.accession import AccessionRepository
from app.domain.entities.accession import Accession


def get_list(term: str) -> None:

    response = AccessionRepository().show(term)
    print(list(response))


def create_accession(payload: Dict[str, Any]) -> Union[bool, Accession]:

    accession = Accession(**payload)
    accession_repo = AccessionRepository()
    return accession.save(accession_repo)
