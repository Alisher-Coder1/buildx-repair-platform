from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

index_path = ROOT / "frontend" / "prototype" / "index.html"
app_path = ROOT / "frontend" / "prototype" / "static" / "app.js"

room_ru = "\u0412\u0430\u043d\u043d\u0430\u044f"
no_price_ru = "\u041d\u0435\u0442 \u0446\u0435\u043d\u044b"
price_accounted_ru = "\u0426\u0435\u043d\u0430 \u0443\u0447\u0442\u0435\u043d\u0430"

print("[INFO] Applying final price UX polish via Python...")

if not index_path.exists():
    raise FileNotFoundError(f"Missing file: {index_path}")

if not app_path.exists():
    raise FileNotFoundError(f"Missing file: {app_path}")

index = index_path.read_text(encoding="utf-8")
index = index.replace('value="Bathroom"', f'value="{room_ru}"')
index = index.replace(">Bathroom<", f">{room_ru}<")
index_path.write_text(index, encoding="utf-8")

app = app_path.read_text(encoding="utf-8")

new_function = (
    "function priceStatusForMaterial(materialId) {\n"
    "  return getPrice(materialId) === null\n"
    f'    ? "{no_price_ru}"\n'
    f'    : "{price_accounted_ru}";\n'
    "}"
)

pattern = r"function priceStatusForMaterial\(materialId\) \{[\s\S]*?\n\}"

if "function priceStatusForMaterial(materialId)" not in app:
    raise RuntimeError("Function priceStatusForMaterial(materialId) was not found in app.js")

app, count = re.subn(pattern, new_function, app, count=1)

if count != 1:
    raise RuntimeError("Could not replace priceStatusForMaterial function safely")

app_path.write_text(app, encoding="utf-8")

print("[OK] index.html updated")
print("[OK] app.js updated")
print("[NEXT] Run: pytest")
