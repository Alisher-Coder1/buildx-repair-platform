from app.domain.room_type_rules import (
    get_default_zone_for_room_type,
    normalize_room_type_code,
    resolve_default_zone_for_room_type,
)


def test_canonical_room_type_default_zones():
    assert get_default_zone_for_room_type("bathroom") == "WET"
    assert get_default_zone_for_room_type("toilet") == "WET"
    assert get_default_zone_for_room_type("kitchen") == "KITCHEN"
    assert get_default_zone_for_room_type("living_room") == "DRY"
    assert get_default_zone_for_room_type("corridor") == "DRY"


def test_ru_room_type_aliases_are_normalized():
    assert normalize_room_type_code("\u0412\u0430\u043d\u043d\u0430\u044f") == "bathroom"
    assert normalize_room_type_code("\u0421\u0430\u043d\u0443\u0437\u0435\u043b") == "toilet"
    assert normalize_room_type_code("\u041a\u0443\u0445\u043d\u044f") == "kitchen"
    assert normalize_room_type_code("\u0417\u0430\u043b") == "living_room"
    assert normalize_room_type_code("\u041a\u043e\u0440\u0438\u0434\u043e\u0440") == "corridor"


def test_ru_room_type_aliases_resolve_default_zones():
    assert resolve_default_zone_for_room_type("\u0412\u0430\u043d\u043d\u0430\u044f") == "WET"
    assert resolve_default_zone_for_room_type("\u0421\u0430\u043d\u0443\u0437\u0435\u043b") == "WET"
    assert resolve_default_zone_for_room_type("\u041a\u0443\u0445\u043d\u044f") == "KITCHEN"
    assert resolve_default_zone_for_room_type("\u0417\u0430\u043b") == "DRY"
    assert resolve_default_zone_for_room_type("\u041a\u043e\u0440\u0438\u0434\u043e\u0440") == "DRY"
