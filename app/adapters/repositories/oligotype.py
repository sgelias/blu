from typing import List, Tuple

from app.adapters.infra.config import DBConnectionHander
from app.adapters.infra.entities import OligotypesModel
from app.domain.entities import Oligotype
from app.domain.repository import OligotypeRepository
from app.domain.exceptions import AlreadyRegisteredOligotype
from dacite import from_dict
from sqlalchemy import update


class OligotypeRepositoryManager(OligotypeRepository):
    """A manager of Oligotype model."""

    @staticmethod
    def add(oligotype: Oligotype) -> Tuple[bool, Oligotype]:
        """Insert a single record into database

        Args:
            oligotype (Oligotype): An oligotype object.

        Returns:
            Tuple[bool, Oligotype]: A boolean indicating if the
                oligotype was created (True) or recovered from database
                (False), and a instance of the created oligotype.
        """

        old_oligotype = OligotypesModel.query.filter(
            OligotypesModel.oligotype == oligotype.oligotype
        ).first()

        if not old_oligotype:
            with DBConnectionHander() as conn:
                try:
                    new_oligotype = OligotypesModel(**oligotype.__dict__)
                    conn.session.add(new_oligotype)
                    conn.session.commit()
                    return True, from_dict(Oligotype, new_oligotype.as_dict())

                except:
                    conn.session.rollback()
                    raise
                finally:
                    conn.session.close_all()

        return False, from_dict(Oligotype, old_oligotype.as_dict())

    @staticmethod
    def show(term: str) -> List[Oligotype]:
        """List oligotype given the search term.

        Args:
            term (str): A term to filter oligotype.

        Returns:
            List[Oligotype]: A list of filtered oligotype.
        """

        if term:
            return [
                from_dict(Oligotype, record.__dict__)
                for record in (
                    OligotypesModel.query.filter(
                        OligotypesModel.oligotype == term
                    ).order_by(OligotypesModel.oligotype.desc())
                )
            ]

        return [
            from_dict(Oligotype, record.__dict__)
            for record in (
                OligotypesModel.query.order_by(OligotypesModel.oligotype.desc())
            )
        ]

    @staticmethod
    def edit(old_oligotype: str, new_oligotype: str) -> Oligotype:
        """Update a existing oligotype

        Args:
            old_oligotype (str): The name of the oligotype to edit.
            new_oligotype (str): The new oligotype name.

        Returns:
            Oligotype: A oligotype instance.
        """

        proposed_oligotype = OligotypesModel.query.filter(
            OligotypesModel.oligotype == new_oligotype
        ).first()

        if proposed_oligotype:
            raise AlreadyRegisteredOligotype(
                f"Oligotype already registered: {new_oligotype}. Select other."
            )

        with DBConnectionHander() as conn:
            try:
                updated_oligotype = (
                    update(OligotypesModel)
                    .where(OligotypesModel.oligotype == old_oligotype)
                    .values(oligotype=new_oligotype)
                )

                conn.session.execute(updated_oligotype)
                conn.session.commit()

                return from_dict(
                    Oligotype,
                    (
                        OligotypesModel.query.filter(
                            OligotypesModel.oligotype == new_oligotype
                        ).first()
                    ).__dict__,
                )

            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close_all()
