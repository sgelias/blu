from src.adapters.infra.config import DBConnectionHander
from src.adapters.repositories import AccessionRepositoryManager
from src.domain.entities import Accession
from faker import Faker

faker = Faker()
accession_repository = AccessionRepositoryManager()
conn_handler = DBConnectionHander()


def test_add_accession():
    """Should insert Accession."""

    data = {
        "accession": faker.word(),
        "title": "Corynebacterium tuberculostearicum strain ",
        "taxid": 38304,
        "sciname": "Corynebacterium tuberculostearicum",
        "sciname_clean": "Corynebacterium tuberculostearicum",
    }

    eng = conn_handler.get_engine()
    accession = Accession(**data)

    # Insert a single record.
    _, new_accession = accession_repository.add(accession)

    # Fetch the inserted record.
    query_accession = eng.execute(
        f"SELECT * FROM blu_accessions WHERE id = '{new_accession.id}';"
    ).fetchone()

    print(new_accession)
    print(query_accession)

    # Compare the record content.
    assert query_accession.id == new_accession.id
    assert query_accession.accession == new_accession.accession
    assert query_accession.title == new_accession.title
    assert query_accession.taxid == new_accession.taxid
    assert query_accession.sciname == new_accession.sciname
    assert query_accession.sciname_clean == new_accession.sciname_clean

    # Delete inserted record.
    eng.execute(f"DELETE FROM blu_accessions WHERE id = '{new_accession.id}';")