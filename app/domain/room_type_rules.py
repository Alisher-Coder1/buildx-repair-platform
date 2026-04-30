from dataclasses import dataclass


@dataclass(frozen=True)
class RoomTypeRule:
    code: str
    label_ru: str
    default_zone: str
    is_wet_room: bool = False
    is_kitchen: bool = False
    is_living_space: bool = False
    is_auxiliary_space: bool = False
    notes: str = ""


ROOM_TYPE_RULES: dict[str, RoomTypeRule] = {
    "bathroom": RoomTypeRule(
        code="bathroom",
        label_ru="\u0412\u0430\u043d\u043d\u0430\u044f",
        default_zone="WET",
        is_wet_room=True,
    ),
    "toilet": RoomTypeRule(
        code="toilet",
        label_ru="\u0421\u0430\u043d\u0443\u0437\u0435\u043b",
        default_zone="WET",
        is_wet_room=True,
    ),
    "kitchen": RoomTypeRule(
        code="kitchen",
        label_ru="\u041a\u0443\u0445\u043d\u044f",
        default_zone="KITCHEN",
        is_kitchen=True,
    ),
    "living_room": RoomTypeRule(
        code="living_room",
        label_ru="\u0417\u0430\u043b",
        default_zone="DRY",
        is_living_space=True,
    ),
    "bedroom": RoomTypeRule(
        code="bedroom",
        label_ru="\u0421\u043f\u0430\u043b\u044c\u043d\u044f",
        default_zone="DRY",
        is_living_space=True,
    ),
    "children_room": RoomTypeRule(
        code="children_room",
        label_ru="\u0414\u0435\u0442\u0441\u043a\u0430\u044f",
        default_zone="DRY",
        is_living_space=True,
    ),
    "corridor": RoomTypeRule(
        code="corridor",
        label_ru="\u041a\u043e\u0440\u0438\u0434\u043e\u0440",
        default_zone="DRY",
        is_auxiliary_space=True,
    ),
    "storage": RoomTypeRule(
        code="storage",
        label_ru="\u041a\u043b\u0430\u0434\u043e\u0432\u043a\u0430",
        default_zone="DRY",
        is_auxiliary_space=True,
    ),
    "balcony_loggia": RoomTypeRule(
        code="balcony_loggia",
        label_ru="\u0411\u0430\u043b\u043a\u043e\u043d / \u043b\u043e\u0434\u0436\u0438\u044f",
        default_zone="DRY",
        is_auxiliary_space=True,
    ),
}


ROOM_TYPE_ALIASES: dict[str, str] = {
    "bathroom": "bathroom",
    "\u0432\u0430\u043d\u043d\u0430\u044f": "bathroom",
    "\u0432\u0430\u043d\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430": "bathroom",

    "toilet": "toilet",
    "\u0441\u0430\u043d\u0443\u0437\u0435\u043b": "toilet",
    "\u0442\u0443\u0430\u043b\u0435\u0442": "toilet",

    "kitchen": "kitchen",
    "\u043a\u0443\u0445\u043d\u044f": "kitchen",

    "living_room": "living_room",
    "living room": "living_room",
    "\u0437\u0430\u043b": "living_room",
    "\u0433\u043e\u0441\u0442\u0438\u043d\u0430\u044f": "living_room",

    "bedroom": "bedroom",
    "\u0441\u043f\u0430\u043b\u044c\u043d\u044f": "bedroom",

    "children_room": "children_room",
    "children room": "children_room",
    "\u0434\u0435\u0442\u0441\u043a\u0430\u044f": "children_room",

    "corridor": "corridor",
    "\u043a\u043e\u0440\u0438\u0434\u043e\u0440": "corridor",

    "storage": "storage",
    "\u043a\u043b\u0430\u0434\u043e\u0432\u043a\u0430": "storage",

    "balcony_loggia": "balcony_loggia",
    "balcony / loggia": "balcony_loggia",
    "\u0431\u0430\u043b\u043a\u043e\u043d": "balcony_loggia",
    "\u043b\u043e\u0434\u0436\u0438\u044f": "balcony_loggia",
    "\u0431\u0430\u043b\u043a\u043e\u043d / \u043b\u043e\u0434\u0436\u0438\u044f": "balcony_loggia",
}


def normalize_room_type_code(room_type_value: str) -> str:
    normalized = room_type_value.strip().lower()

    if normalized in ROOM_TYPE_ALIASES:
        return ROOM_TYPE_ALIASES[normalized]

    for code, rule in ROOM_TYPE_RULES.items():
        if normalized == rule.label_ru.strip().lower():
            return code

    return normalized


def get_room_type_rule(room_type_code: str) -> RoomTypeRule:
    normalized_code = normalize_room_type_code(room_type_code)

    try:
        return ROOM_TYPE_RULES[normalized_code]
    except KeyError as exc:
        raise ValueError(f"Unknown room type code: {room_type_code}") from exc
def get_default_zone_for_room_type(room_type_code: str) -> str:
    return get_room_type_rule(room_type_code).default_zone


def resolve_default_zone_for_room_type(room_type_value: str) -> str:
    return get_default_zone_for_room_type(room_type_value)


def list_room_type_rules() -> list[RoomTypeRule]:
    return list(ROOM_TYPE_RULES.values())
