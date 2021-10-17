from app.settings import SQLITE_DATABASE
from peewee import Model, SqliteDatabase


def initialize_database():

    if SQLITE_DATABASE is not None:
        return SqliteDatabase(
            SQLITE_DATABASE, pragmas={"journal_mode": "wal", "cache_size": -1024 * 64}
        )


database = initialize_database()


class BaseModel(Model):
    class Meta:
        database = database
