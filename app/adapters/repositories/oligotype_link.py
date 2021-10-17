from typing import List

from app.adapters.infra.config import DBConnectionHander
from app.adapters.infra.entities import NamespacedOligotypesModel
from app.domain.entities import Namespace, Oligotype, NamespacesdOligotype
from app.domain.repository import NamespacesdOligotypeRepository
from dacite import from_dict


class NamespacesdOligotypeRepositoryManager(NamespacesdOligotypeRepository):
    """A manager of Namespaced Oligotypes model."""

    @staticmethod
    def add(oligotype: Oligotype, namespace: Namespace) -> NamespacesdOligotype:
        """Insert a single record into database.

        Args:
            oligotype (Oligotype): A single oligotype instance.
            namespace (Namespace): A single namespace instance.

        Returns:
            NamespacesdOligotype: A namespaced oligotype instance.
        """

        with DBConnectionHander() as conn:
            try:
                namespaced_oligotype = NamespacedOligotypesModel(
                    namespace=namespace, oligotype=oligotype
                )

                conn.session.add(namespaced_oligotype)
                conn.session.commit()

                return NamespacesdOligotype(
                    id=namespaced_oligotype.id,
                    namespace=namespaced_oligotype.namespace,
                    oligotype=namespaced_oligotype.oligotype,
                )

            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()

    @staticmethod
    def show(term: str) -> List[NamespacesdOligotype]:
        """List namespaced oligotypes given the search term.

        Args:
            term (str): A term to filter namespace oligotypes.

        Returns:
            List[NamespacesdOligotype]: A list of filtered namespace oligotype.
        """

        if term:
            return [
                from_dict(NamespacesdOligotype, record.__dict__)
                for record in (
                    NamespacedOligotypesModel.query.filter(
                        (NamespacedOligotypesModel.namespace == term)
                        | (NamespacedOligotypesModel.oligotype == term)
                    ).order_by(
                        NamespacedOligotypesModel.namespace.desc(),
                        NamespacedOligotypesModel.oligotype.desc(),
                    )
                )
            ]

        return [
            from_dict(Namespace, record.__dict__)
            for record in (
                NamespacedOligotypesModel.query.order_by(
                    NamespacedOligotypesModel.namespace.desc(),
                    NamespacedOligotypesModel.oligotype.desc(),
                )
            )
        ]
