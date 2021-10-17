from typing import List

from app.adapters.infra.config import DBConnectionHander
from app.adapters.infra.entities import NamespacesModel
from app.domain.entities import Namespace
from app.domain.repository import NamespaceRepository
from dacite import from_dict
from sqlalchemy import update


class NamespaceRepositoryManager(NamespaceRepository):
    """A manager of Namespaces model."""

    @staticmethod
    def add(namespace: Namespace) -> Namespace:
        """Insert a single record into database

        Args:
            namespace (Namespace): An namespace object.

        Returns:
            Namespace: A instance of the created namespace.
        """

        with DBConnectionHander() as conn:
            try:
                namespace = NamespacesModel(**namespace.__dict__)
                conn.session.add(namespace)
                conn.session.commit()

                return Namespace(
                    id=namespace.id,
                    namespace=namespace.namespace,
                )

            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()

    @staticmethod
    def show(term: str) -> List[Namespace]:
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
