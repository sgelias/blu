import click

from .accession import get_list

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
