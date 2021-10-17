from app.adapters.infra.config import Base, DBConnectionHander
from app.adapters.infra.entities import *  # noqa: F401, F403
from app.ports.cli import nop_cmds


@nop_cmds.command("initdb")
def init_db():

    eng = DBConnectionHander().get_engine()
    Base.metadata.create_all(eng)
    print(f"Database created at: {eng}")


def main():
    nop_cmds()


if __name__ == "__main__":
    nop_cmds()
