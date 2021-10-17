import click

from .accession import get_list, create_accession

__version__ = "2.0.0"


# -----------------------------------------------------------------------------
# ROOT
# -----------------------------------------------------------------------------


@click.group()
@click.version_option(version=__version__)
def nop_cmds():
    ...


# -----------------------------------------------------------------------------
# ACCESSIONS
# -----------------------------------------------------------------------------


@nop_cmds.command("list")
@click.argument("term", required=True, type=str)
def show(**kwargs) -> None:
    get_list(**kwargs)


@nop_cmds.command("new")
def new(**kwargs) -> None:

    data = {
        # "id": "gi|1948552484|gb|CP065972.1|",
        "accession": "CP065972",
        "title": "Corynebacterium tuberculostearicum strain ",
        "taxid": 38304,
        "sciname": "Corynebacterium tuberculostearicum",
        "sciname_clean": "Corynebacterium tuberculostearicum",
    }

    create_accession(data)
