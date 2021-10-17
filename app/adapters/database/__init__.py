from .base_model import database
from .accessions_model import AccessionModel

models_list = (AccessionModel,)

__all__ = ("database",)
