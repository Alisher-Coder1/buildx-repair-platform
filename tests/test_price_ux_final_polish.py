def test_prototype_default_room_name_is_localized(client):
    response = client.get("/prototype")

    assert response.status_code == 200
    assert "Ванная" in response.text
    assert 'value="Bathroom"' not in response.text


def test_procurement_price_status_labels_are_clear(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert "Цена учтена" in response.text
    assert "Нет цены" in response.text
    assert "function priceStatusForMaterial" in response.text
