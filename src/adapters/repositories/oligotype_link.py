from typing import List, Tuple

from src.adapters.infra.config import DBConnectionHander
from src.adapters.infra.models import NamespacedOligotypesModel
from src.domain.data_stores import NamespacedOligotype
from src.domain.repository import NamespacedOligotypeRepository
from dacite import from_dict


class NamespacesdOligotypeRepositoryManager(NamespacedOligotypeRepository):
    """A manager of Namespaced Oligotypes model."""

    @staticmethod
    def get_or_create(
        namespaced_oligotype: NamespacedOligotype,
    ) -> Tuple[bool, NamespacedOligotype]:
        """Insert a single record into database.

        Args:
            namespaced_oligotype (NamespacedOligotype): A single namespaced
                oligotype entity.

        Returns:
            Tuple[bool, NamespacesdOligotype]: A boolean indicating if the
                namespace was created (True) or recovered from database
                (False), and a instance of the created namespaced oligotype.
        """

        old_namespaced_oligotype = NamespacedOligotypesModel.query.filter(
            (NamespacedOligotypesModel.namespace == namespaced_oligotype.namespace)
            & (NamespacedOligotypesModel.oligotype == namespaced_oligotype.oligotype)
        ).first()

        if old_namespaced_oligotype:
            return False, from_dict(
                NamespacedOligotype, old_namespaced_oligotype.as_dict()
            )

        with DBConnectionHander() as conn:
            try:
                new_namespaced_oligotype = NamespacedOligotypesModel(
                    **namespaced_oligotype.__dict__
                )

                conn.session.add(namespaced_oligotype)
                conn.session.commit()
                return True, from_dict(
                    NamespacedOligotype, new_namespaced_oligotype.as_dict()
                )

            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()

    @staticmethod
    def show(term: str) -> List[NamespacedOligotype]:
        """List namespaced oligotypes given the search term.

        Args:
            term (str): A term to filter namespace oligotypes.

        Returns:
            List[NamespacesdOligotype]: A list of filtered namespace oligotype.
        """

        if term:
            return [
                from_dict(NamespacedOligotype, record.__dict__)
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
            from_dict(NamespacedOligotype, record.__dict__)
            for record in (
                NamespacedOligotypesModel.query.order_by(
                    NamespacedOligotypesModel.namespace.desc(),
                    NamespacedOligotypesModel.oligotype.desc(),
                )
            )
        ]
