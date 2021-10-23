from src.adapters.infra.config import DBConnectionHander
from src.adapters.repositories import OligotypeRepositoryManager
from src.domain.data_stores import Oligotype
from faker import Faker

faker = Faker()
oligotype_repository = OligotypeRepositoryManager()
conn_handler = DBConnectionHander()


def test_add_oligotype():
    """Should insert Oligotype."""

    data = {
        "oligotype": faker.word(),
    }

    eng = conn_handler.get_engine()
    oligotype = Oligotype(**data)

    # Insert a single record.
    new_created, new_oligotype = oligotype_repository.get_or_create(oligotype)

    # Get an existent record.
    non_new_created, non_new_oligotype = oligotype_repository.get_or_create(oligotype)

    # Fetch the inserted record.
    query_oligotype = eng.execute(
        f"SELECT * FROM blu_oligotypes WHERE id = '{new_oligotype.id}';"
    ).fetchone()

    print(new_oligotype)
    print(query_oligotype)

    # Compare the record content.
    assert new_created is True
    assert non_new_created is False
    assert new_oligotype == non_new_oligotype
    assert query_oligotype.id == new_oligotype.id
    assert query_oligotype.oligotype == new_oligotype.oligotype
    assert not query_oligotype.is_default_oligotype

    if query_oligotype.is_default_oligotype:
        assert query_oligotype.oligotype_code != new_oligotype.oligotype_code

    # Delete inserted record.
    eng.execute(f"DELETE FROM blu_oligotypes WHERE id = '{new_oligotype.id}';")
