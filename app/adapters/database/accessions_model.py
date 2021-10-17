from peewee import CharField, IntegerField, TextField, UUIDField

from .base_model import BaseModel


class AccessionModel(BaseModel):

    accession_id = UUIDField(primary_key=True)
    accession = CharField(max_length=15, unique=True)
    title = TextField()
    taxid = IntegerField(null=True)
    sciname = CharField()
    sciname_clean = CharField(null=True)

    class Meta:
        table_name = "nop_accession"
