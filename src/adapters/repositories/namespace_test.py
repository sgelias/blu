from src.adapters.infra.config import DBConnectionHander
from src.adapters.repositories import NamespaceRepositoryManager
from src.domain.data_stores import Namespace
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
    new_created, new_namespace = namespace_repository.get_or_create(namespace)

    # Get an existent record.
    non_new_created, non_new_namespace = namespace_repository.get_or_create(namespace)

    # Fetch the inserted record.
    query_namespace = eng.execute(
        f"SELECT * FROM blu_namespaces WHERE id = '{new_namespace.id}';"
    ).fetchone()

    print(new_namespace)
    print(query_namespace)

    # Compare the record content.
    assert new_created is True
    assert non_new_created is False
    assert new_namespace == non_new_namespace
    assert query_namespace.id == new_namespace.id
    assert query_namespace.namespace == new_namespace.namespace

    # Delete inserted record.
    eng.execute(f"DELETE FROM blu_namespaces WHERE id = '{new_namespace.id}';")
