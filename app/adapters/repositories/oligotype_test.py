from app.adapters.infra.config import DBConnectionHander
from app.adapters.repositories import OligotypeRepositoryManager
from app.domain.entities import Oligotype
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
    new_oligotype = oligotype_repository.add(oligotype)

    # Fetch the inserted record.
    query_oligotype = eng.execute(
        f"SELECT * FROM nop_oligotypes WHERE id = '{new_oligotype.id}';"
    ).fetchone()

    print(new_oligotype)
    print(query_oligotype)

    # Compare the record content.
    assert query_oligotype.id == new_oligotype.id
    assert query_oligotype.oligotype == new_oligotype.oligotype
    assert query_oligotype.oligotype_code == new_oligotype.oligotype_code
    assert query_oligotype.is_default_oligotype == new_oligotype.is_default_oligotype
    assert not query_oligotype.is_default_oligotype

    # Delete inserted record.
    eng.execute(f"DELETE FROM nop_oligotypes WHERE id = '{new_oligotype.id}';")
