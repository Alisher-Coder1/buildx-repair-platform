from pathlib import Path

from app.artifacts.loader import REQUIRED_ARTIFACT_FILES, load_artifact_set, load_json_file


def test_required_artifact_files_exist():
    artifact_dir = Path("data/artifacts")

    for filename in REQUIRED_ARTIFACT_FILES:
        assert (artifact_dir / filename).exists(), f"Missing artifact file: {filename}"


def test_load_artifact_set_success():
    artifact_set = load_artifact_set()

    assert "coatings_v1.json" in artifact_set
    assert "materials_v1.json" in artifact_set
    assert "operation_material_rules_v1.json" in artifact_set


def test_load_json_file_success():
    data = load_json_file(Path("data/artifacts/materials_v1.json"))

    assert data["artifact_name"] == "materials"
    assert isinstance(data["items"], list)
