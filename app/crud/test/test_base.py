import pytest
import logging

from mock import MagicMock
from app.models import Item
from app.crud.base import CRUDBase


mocked_model = MagicMock()
mock_session = MagicMock()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

test_id = 1


@pytest.fixture
def test_base():
    return CRUDBase(Item)


@pytest.mark.unit
def test_get_returns_something(test_base: CRUDBase):
    res = test_base.get(mock_session, test_id)
    assert res is not None
