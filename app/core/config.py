from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_DIR = BASE_DIR / "runtime"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_DIR / 'buildx.sqlite3'}"

API_TITLE = "Buildx Repair Platform API"
API_VERSION = "prototype_v0.1"
API_PREFIX = "/api/v1"
