def test_frontend_js_contains_price_input_logic(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert "PRICE_STORAGE_KEY" in response.text
    assert "price-input" in response.text
    assert "calculateCostRows" in response.text
    assert "calculateCostTotal" in response.text
    assert "Цена за упаковку" in response.text
    assert "Предварительная сумма" in response.text


def test_frontend_js_contains_price_status_labels(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert "PRICE_ENTERED" in response.text
    assert "Цена введена" in response.text
    assert "Цена не указана" in response.text


def test_frontend_css_contains_price_input_styles(client):
    response = client.get("/prototype/static/styles.css")

    assert response.status_code == 200
    assert "price-input" in response.text
    assert "cost-total-card" in response.text
    assert "total-card" in response.text
