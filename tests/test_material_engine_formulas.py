import pytest

from app.artifacts.exceptions import ArtifactValidationError
from app.domain.material_engine import calculate_material_quantity, calculate_package_count


def test_calculate_package_count_rounds_up():
    assert calculate_package_count(12.96, 2.0) == 7


def test_calculate_package_count_minimum_one():
    assert calculate_package_count(0.1, 10.0) == 1


def test_calculate_package_count_invalid_package_size():
    with pytest.raises(ArtifactValidationError) as exc:
        calculate_package_count(10.0, 0)

    assert exc.value.error_code == "ERR_PACKAGE_SIZE_MISSING"


def test_layer_based_quantity():
    quantity = calculate_material_quantity(
        formula_type="LAYER_BASED",
        base_quantity=37.8,
        norm={"consumption_norm": 0.15, "default_layer_count": 2, "default_loss_factor": 1.10},
        rule={"rule_id": "RULE_WALL_PAINT", "norm_id": "NORM_PAINT", "layer_count": 2, "loss_factor": 1.10},
    )

    assert round(quantity, 2) == 12.47


def test_thickness_based_quantity():
    quantity = calculate_material_quantity(
        formula_type="THICKNESS_BASED",
        base_quantity=37.8,
        norm={"q_per_mm": 1.0, "default_loss_factor": 1.10},
        rule={"rule_id": "RULE_WALL_PUTTY", "norm_id": "NORM_PUTTY", "thickness_mm": 2, "loss_factor": 1.10},
    )

    assert round(quantity, 2) == 83.16
