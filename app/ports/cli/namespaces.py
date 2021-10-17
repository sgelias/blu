from typing import Any, Dict

from app.adapters.repositories import NamespaceRepositoryManager
from app.domain.entities import Namespace


def get_namespaces_list(term: str) -> None:

    response = NamespaceRepositoryManager().show(term)
    for r in response:
        print(r)


def create_namespace(namespace: Dict[str, Any]) -> None:

    namespace = Namespace(namespace=namespace)
    namespace_repo = NamespaceRepositoryManager()
    new_namespace = namespace.save(namespace_repo)
    print(new_namespace)


def update_namespace(old_namespace: str, new_namespace: str) -> None:

    response = NamespaceRepositoryManager().edit(old_namespace, new_namespace)
    print(response)
