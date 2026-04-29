import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

TEST_DB = Path("runtime/test_buildx.sqlite3")
os.environ["TESTING"] = "1"

from app.db.models import Base
from app.db.session import engine
from app.main import app


@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)
