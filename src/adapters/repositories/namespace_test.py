from src.adapters.infra.config import DBConnectionHander
from src.adapters.repositories import NamespaceRepositoryManager
from src.domain.entities import Namespace
from faker import Faker

faker = Faker()
namespace_repository = NamespaceRepositoryManager()
conn_handler = DBConnectionHander()


def test_add_namespace():
    """Should insert Namespace."""

    data = {
        "namespace": faker.word(),
    }

    eng = conn_handler.get_engine()
    namespace = Namespace(**data)

    # Insert a single record.
    _, new_namespace = namespace_repository.add(namespace)
    print(new_namespace)

    # Fetch the inserted record.
    query_namespace = eng.execute(
        f"SELECT * FROM blu_namespaces WHERE id = '{new_namespace.id}';"
    ).fetchone()

    print(new_namespace)
    print(query_namespace)

    # Compare the record content.
    assert query_namespace.id == new_namespace.id
    assert query_namespace.namespace == new_namespace.namespace

    # Delete inserted record.
    eng.execute(f"DELETE FROM blu_namespaces WHERE id = '{new_namespace.id}';")