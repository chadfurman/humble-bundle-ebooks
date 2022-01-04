from dto.bundle import BundleDTO
from repositories.bundle import BundleRepository
from database.db_manager import dal
from database.models.bundle import Bundle
from dto.bundle import BundleDTO as BundleDTO
from datetime import datetime
import pytest

@pytest.fixture()
def fake_dal():
    dal.init_db(test=True)
    yield dal
    dal.teardown()

@pytest.fixture()
def fake_bundle(fake_dal):
    yield BundleDTO(
            bundle_id=1,
            bundle_name="Test Bundle",  # String, description="A human-readable name for this bundle")
            amount_spent=10.01,
            gamekey="TEST_GAME_KEY",
            uid="X9GHPP9ABKS28",
            created=datetime.strptime('2019-12-06T06:58:10',"%Y-%m-%dT%H:%M:%S"),
            total_choices=1,
            choices_remaining=0,
            currency="USD",
            is_giftee=False,
            claimed=True,
            total=10.01,
            path_ids="",
        )


def test_bundle_repository_can_get_by_id(fake_bundle, fake_dal):
    with fake_dal.get_session() as session:
        session.add(BundleRepository.from_dto(fake_bundle))
        session.commit()
    b = BundleRepository.get_by_id(bundle_id=1)
    assert b.bundle_name == fake_bundle.bundle_name


def test_bundle_repository_can_create(fake_bundle, fake_dal):
    b = BundleRepository.get_by_id(bundle_id=1)
    assert b is None
    BundleRepository.create(fake_bundle)
    b = BundleRepository.get_by_id(bundle_id=1)
    assert b.bundle_name == fake_bundle.bundle_name


def test_bundle_repository_can_update(fake_bundle, fake_dal):
    BundleRepository.create(fake_bundle)
    b = BundleRepository.get_by_id(bundle_id=1)
    assert b.bundle_name == fake_bundle.bundle_name
    fake_bundle.bundle_name = "New Name"
    assert b.bundle_name != fake_bundle.bundle_name
    b = BundleRepository.update(fake_bundle)
    assert b.bundle_name == "New Name"


def test_bundle_repository_can_delete(fake_bundle, fake_dal):
    b = BundleRepository.create(fake_bundle)
    BundleRepository.delete(b)
    assert BundleRepository.get_by_id(bundle_id=1) is None

