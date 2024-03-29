from typing import List, Tuple

from src.adapters.infra.config import DBConnectionHander
from src.adapters.infra.models import NamespacesModel
from src.domain.data_stores import Namespace
from src.domain.repositories import NamespaceRepository
from dacite import from_dict
from sqlalchemy import update


class NamespaceRepositoryManager(NamespaceRepository):
    """A manager of Namespaces model."""

    @classmethod
    def get_or_create(cls, namespace: Namespace) -> Tuple[bool, Namespace]:
        """Insert a single record into database

        Args:
            namespace (Namespace): An namespace object.

        Returns:
            Tuple[bool, Namespace]: A boolean indicating if the namespace was
                created (True) or recovered from database (False), and a
                instance of the created namespace.
        """

        old_namespace = NamespacesModel.query.filter(
            NamespacesModel.namespace == namespace.namespace
        ).first()

        if old_namespace:
            return False, from_dict(Namespace, old_namespace.as_dict())

        with DBConnectionHander() as conn:
            try:
                new_namespace = NamespacesModel(**namespace.__dict__)
                conn.session.add(new_namespace)
                conn.session.commit()
                return True, from_dict(Namespace, new_namespace.as_dict())

            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()

    @classmethod
    def show(cls, term: str) -> List[Namespace]:
        """List namespaces given the search term.

        Args:
            term (str): A term to filter namespaces.

        Returns:
            List[Namespace]: A list of filtered namespaces.
        """

        if term:
            return [
                from_dict(Namespace, record.__dict__)
                for record in (
                    NamespacesModel.query.filter(
                        NamespacesModel.namespace == term
                    ).order_by(NamespacesModel.namespace.desc())
                )
            ]

        return [
            from_dict(Namespace, record.__dict__)
            for record in (
                NamespacesModel.query.order_by(NamespacesModel.namespace.desc())
            )
        ]

    @staticmethod
    def edit(old_namespace: str, new_namespace: str) -> Namespace:
        """Update a existing namespace

        Args:
            old_namespace (str): The name of the namespace to edit.
            new_namespace (str): The new namespace name.

        Returns:
            Namespace: A namespace instance.
        """

        proposed_namespace = NamespacesModel.query.filter(
            NamespacesModel.namespace == new_namespace
        ).first()

        if proposed_namespace:
            raise ValueError(
                f"Namespace also registered: {new_namespace}. Select other."
            )

        with DBConnectionHander() as conn:
            try:
                updated_namespace = (
                    update(NamespacesModel)
                    .where(NamespacesModel.namespace == old_namespace)
                    .values(namespace=new_namespace)
                )

                conn.session.execute(updated_namespace)
                conn.session.commit()

                return from_dict(
                    Namespace,
                    (
                        NamespacesModel.query.filter(
                            NamespacesModel.namespace == new_namespace
                        ).first()
                    ).__dict__,
                )

            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()
