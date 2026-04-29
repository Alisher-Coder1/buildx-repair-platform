import copy
from pathlib import Path

import pytest

from app.artifacts.exceptions import ArtifactValidationError
from app.artifacts.loader import load_artifact_set
from app.artifacts.validators import validate_artifact_set


def test_artifact_references_are_valid():
    artifact_set = load_artifact_set()

    validate_artifact_set(artifact_set)


def test_duplicate_material_id_returns_error():
    artifact_set = load_artifact_set()
    materials = artifact_set["materials_v1.json"]["items"]
    materials.append(copy.deepcopy(materials[0]))

    with pytest.raises(ArtifactValidationError) as exc:
        validate_artifact_set(artifact_set)

    assert exc.value.error_code == "ERR_ARTIFACT_DUPLICATE_ID"


def test_broken_rule_material_reference_returns_error():
    artifact_set = load_artifact_set()
    artifact_set["operation_material_rules_v1.json"]["items"][0]["material_id"] = "MAT_DOES_NOT_EXIST"

    with pytest.raises(ArtifactValidationError) as exc:
        validate_artifact_set(artifact_set)

    assert exc.value.error_code == "ERR_ARTIFACT_REFERENCE_INVALID"


def test_missing_artifact_file_returns_error(tmp_path: Path):
    from app.artifacts.loader import load_artifact_set

    with pytest.raises(ArtifactValidationError) as exc:
        load_artifact_set(tmp_path)

    assert exc.value.error_code == "ERR_ARTIFACT_FILE_MISSING"


def test_invalid_formula_norm_missing_q_per_mm_returns_error():
    artifact_set = load_artifact_set()
    norms = artifact_set["material_norms_v1.json"]["items"]

    target = next(item for item in norms if item["formula_type"] == "THICKNESS_BASED")
    target.pop("q_per_mm", None)

    with pytest.raises(ArtifactValidationError) as exc:
        validate_artifact_set(artifact_set)

    assert exc.value.error_code == "ERR_ARTIFACT_REQUIRED_FIELD_MISSING"
