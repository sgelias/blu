import click

from .accessions import get_accessions_list
from .namespaces import create_namespace, get_namespaces_list, update_namespace
from .oligotype_links import get_namespaced_oligotypes_list
from .oligotypes import create_oligotype, get_oligotypes_list, update_oligotype

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


# -----------------------------------------------------------------------------
# OLIGOTYPES
# -----------------------------------------------------------------------------


@nop_cmds.group("oligo", help="Oligotypes associated tools.")
def oligotypes_cmds():
    ...


@oligotypes_cmds.command("list")
@click.argument("term", required=False, type=str, default=None)
def get_oligotypes_list_cli(**kwargs) -> None:
    get_oligotypes_list(**kwargs)


@oligotypes_cmds.command("new")
@click.argument("oligotype", required=True, type=str)
def create_oligotype_cli(**kwargs) -> None:
    create_oligotype(**kwargs)


@oligotypes_cmds.command("edit")
@click.option(
    "--old-oligotype", "-o", required=True, type=str, help="The oligotype to edit."
)
@click.option(
    "--new-oligotype", "-n", required=True, type=str, help="The new oligotype name."
)
def update_oligotype_cli(**kwargs) -> None:
    update_oligotype(**kwargs)


# -----------------------------------------------------------------------------
# OLIGOTYPE LINKS
# -----------------------------------------------------------------------------


@nop_cmds.group("ol", help="Oligotypes links associated tools.")
def oligotype_links_cmds():
    ...


@oligotype_links_cmds.command("list")
@click.argument("term", required=False, type=str, default=None)
def get_namespaced_oligotypes_list_cli(**kwargs) -> None:
    get_namespaced_oligotypes_list(**kwargs)
