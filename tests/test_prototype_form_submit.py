from pathlib import Path


def test_calculate_button_is_not_submit_button():
    html = Path("frontend/prototype/index.html").read_text(encoding="utf-8")

    assert 'id="calculateButton"' in html
    assert 'type="button"' in html


def test_room_form_submit_is_prevented():
    js = Path("frontend/prototype/static/app.js").read_text(encoding="utf-8")

    assert 'addEventListener("submit"' in js
    assert "preventDefault()" in js
