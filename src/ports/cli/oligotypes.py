from typing import Any, Dict

from src.adapters.repositories import OligotypeRepositoryManager
from src.domain.entities import Oligotype


def get_oligotypes_list(term: str) -> None:

    response = OligotypeRepositoryManager().show(term)
    for r in response:
        print(r)


def create_oligotype(oligotype: Dict[str, Any]) -> None:

    oligotype = Oligotype(oligotype=oligotype)
    oligotype_repo = OligotypeRepositoryManager()
    new_oligotype = oligotype.save(oligotype_repo)
    print(new_oligotype)


def update_oligotype(old_oligotype: str, new_oligotype: str) -> None:

    response = OligotypeRepositoryManager().edit(old_oligotype, new_oligotype)
    print(response)
