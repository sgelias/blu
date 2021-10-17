from app.adapters.database import database, models_list
from app.ports.cli import nop_cmds


data = {
    # "id": "gi|1948552484|gb|CP065972.1|",
    "accession": "CP065972",
    "title": "Corynebacterium tuberculostearicum strain FDAARGOS_993 chromosome, complete genome",
    "taxid": 38304,
    "sciname": "Corynebacterium tuberculostearicum",
    "sciname_clean": "Corynebacterium tuberculostearicum",
}


def main():
    database.connect()
    database.create_tables(models_list)
    nop_cmds()
    database.close()


if __name__ == "__main__":
    nop_cmds()
