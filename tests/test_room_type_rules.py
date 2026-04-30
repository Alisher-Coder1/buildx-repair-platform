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
        label_ru="Ванная",
        default_zone="WET",
        is_wet_room=True,
        notes="Влажное помещение. Требует будущих правил гидроизоляции, вентиляции и сантехники.",
    ),
    "toilet": RoomTypeRule(
        code="toilet",
        label_ru="Санузел",
        default_zone="WET",
        is_wet_room=True,
        notes="Влажное помещение. Требует будущих правил сантехники, вентиляции и гидроизоляции.",
    ),
    "kitchen": RoomTypeRule(
        code="kitchen",
        label_ru="Кухня",
        default_zone="KITCHEN",
        is_kitchen=True,
        notes="Кухонная зона. В будущем влияет на вентиляцию, электрику, сантехнику и мебель.",
    ),
    "living_room": RoomTypeRule(
        code="living_room",
        label_ru="Зал",
        default_zone="DRY",
        is_living_space=True,
    ),
    "bedroom": RoomTypeRule(
        code="bedroom",
        label_ru="Спальня",
        default_zone="DRY",
        is_living_space=True,
    ),
    "children_room": RoomTypeRule(
        code="children_room",
        label_ru="Детская",
        default_zone="DRY",
        is_living_space=True,
    ),
    "corridor": RoomTypeRule(
        code="corridor",
        label_ru="Коридор",
        default_zone="DRY",
        is_auxiliary_space=True,
    ),
    "storage": RoomTypeRule(
        code="storage",
        label_ru="Кладовка",
        default_zone="DRY",
        is_auxiliary_space=True,
    ),
    "balcony_loggia": RoomTypeRule(
        code="balcony_loggia",
        label_ru="Балкон / лоджия",
        default_zone="DRY",
        is_auxiliary_space=True,
        notes="Будущий особый тип помещения: утепление, остекление, влажность, ограничения по отоплению.",
    ),
}


def get_room_type_rule(room_type_code: str) -> RoomTypeRule:
    try:
        return ROOM_TYPE_RULES[room_type_code]
    except KeyError as exc:
        raise ValueError(f"Unknown room type code: {room_type_code}") from exc


def get_default_zone_for_room_type(room_type_code: str) -> str:
    return get_room_type_rule(room_type_code).default_zone


def list_room_type_rules() -> list[RoomTypeRule]:
    return list(ROOM_TYPE_RULES.values())