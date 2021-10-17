from os import getenv, path


# ------------------------------------------------------------------------------
# Change DEBUG mode status:
#
# If True when exceptions raised the full traceback is show. Otherwise, only the
# error message is returned to user.
# ------------------------------------------------------------------------------


DEBUG = True


# ------------------------------------------------------------------------------
# Define default application paths.
# ------------------------------------------------------------------------------


GLOBAL_NOP_DIRECTORY = getenv("GLOBAL_NOP_DIRECTORY")

if not GLOBAL_NOP_DIRECTORY:
    GLOBAL_NOP_DIRECTORY = f"{path.expanduser('~')}/.nop"


# ------------------------------------------------------------------------------
# Store URI strings and default database connection path.
# ------------------------------------------------------------------------------


# SQLITE_DATABASE = f"{GLOBAL_NOP_DIRECTORY}/nop.db"
SQLITE_DATABASE = "/home/sgelias/Neoprospecta/Bioinfo/nop-v2/nop.db"
