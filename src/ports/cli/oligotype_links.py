from src.adapters.repositories import NamespacesdOligotypeRepositoryManager


def get_namespaced_oligotypes_list(term: str) -> None:

    response = NamespacesdOligotypeRepositoryManager().show(term)
    for r in response:
        print(r)
