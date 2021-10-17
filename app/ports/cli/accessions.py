from app.adapters.repositories import AccessionRepositoryManager


def get_accessions_list(term: str) -> None:

    response = AccessionRepositoryManager().show(term)
    for r in response:
        print(r)
