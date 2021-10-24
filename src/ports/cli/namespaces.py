from src.adapters.repositories import NamespaceRepositoryManager
from src.domain.data_stores import Namespace


def get_namespaces_list(term: str) -> None:

    response = NamespaceRepositoryManager().show(term)
    for r in response:
        print(r)


def create_namespace(namespace: str) -> None:

    new_namespace = Namespace(namespace=namespace)
    namespace_repo = NamespaceRepositoryManager()
    new_namespace = new_namespace.save(namespace_repo)
    print(new_namespace)


def update_namespace(old_namespace: str, new_namespace: str) -> None:

    response = NamespaceRepositoryManager().edit(old_namespace, new_namespace)
    print(response)
