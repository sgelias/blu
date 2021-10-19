from app.adapters.infra.config import Base, DBConnectionHander
from app.adapters.infra.entities import *  # noqa: F401, F403
from app.ports.cli import blu_cmds


@blu_cmds.command("initdb", help="Initialize database if not exists.")
def init_db():

    eng = DBConnectionHander().get_engine()
    Base.metadata.create_all(eng)
    print(f"Database created at: {eng.url}")


def main():
    blu_cmds()


if __name__ == "__main__":
    main()
