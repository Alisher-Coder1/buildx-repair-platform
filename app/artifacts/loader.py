import json
from pathlib import Path
from typing import Any

from app.artifacts.exceptions import ArtifactValidationError
from app.artifacts.validators import validate_artifact_set

DEFAULT_ARTIFACT_DIR = Path(__file__).resolve().parents[2] / "data" / "artifacts"

REQUIRED_ARTIFACT_FILES = [
    "artifact_manifest_v1.json",
    "coatings_v1.json",
    "materials_v1.json",
    "packages_v1.json",
    "operations_v1.json",
    "material_norms_v1.json",
    "operation_material_rules_v1.json",
]


def load_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_FILE_MISSING",
            message="Artifact file is missing.",
            artifact_file=str(path),
            details={"path": str(path)},
        )

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_JSON_INVALID",
            message="Artifact JSON is invalid.",
            artifact_file=str(path),
            details={"error": str(exc)},
        ) from exc

    if not isinstance(data, dict):
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_JSON_INVALID",
            message="Artifact root must be a JSON object.",
            artifact_file=str(path),
        )

    return data


def load_artifact_set(artifact_dir: Path | str = DEFAULT_ARTIFACT_DIR) -> dict[str, dict[str, Any]]:
    artifact_dir = Path(artifact_dir)
    artifacts: dict[str, dict[str, Any]] = {}

    for filename in REQUIRED_ARTIFACT_FILES:
        artifacts[filename] = load_json_file(artifact_dir / filename)

    validate_artifact_set(artifacts)
    return artifacts


def load_artifact_items(artifact_dir: Path | str = DEFAULT_ARTIFACT_DIR) -> dict[str, list[dict[str, Any]]]:
    artifact_set = load_artifact_set(artifact_dir)
    return {
        filename: artifact.get("items", [])
        for filename, artifact in artifact_set.items()
        if filename != "artifact_manifest_v1.json"
    }
