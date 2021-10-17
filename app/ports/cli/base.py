import click

from .accessions import get_accessions_list
from .namespaces import create_namespace, get_namespaces_list, update_namespace

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


@nop_cmds.group("acc", help="Accessions associated tools.")
def accessions_cmds():
    ...


@accessions_cmds.command("list")
@click.argument("term", required=False, type=str, default=None)
def get_accessions_list_cli(**kwargs) -> None:
    get_accessions_list(**kwargs)


# -----------------------------------------------------------------------------
# NAMESPACES
# -----------------------------------------------------------------------------


@nop_cmds.group("ns", help="Namespace associated tools.")
def namespaces_cmds():
    ...


@namespaces_cmds.command("list")
@click.argument("term", required=False, type=str, default=None)
def get_namespaces_list_cli(**kwargs) -> None:
    get_namespaces_list(**kwargs)


@namespaces_cmds.command("new")
@click.argument("namespace", required=True, type=str)
def create_namespace_cli(**kwargs) -> None:
    create_namespace(**kwargs)


@namespaces_cmds.command("edit")
@click.option(
    "--old-namespace", "-o", required=True, type=str, help="The namespace to edit."
)
@click.option(
    "--new-namespace", "-n", required=True, type=str, help="The new namespace name."
)
def update_namespace_cli(**kwargs) -> None:
    update_namespace(**kwargs)
