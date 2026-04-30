def test_frontend_contains_overview_block(client):
    response = client.get("/prototype")

    assert response.status_code == 200
    assert "Краткая сводка" in response.text
    assert "resultOverview" in response.text


def test_frontend_js_contains_russian_labels(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert "Гидроизоляция пола" in response.text
    assert "Керамогранит" in response.text
    assert "Цена не указана" in response.text
    assert "humanError" in response.text


def test_frontend_css_contains_warning_explanation_styles(client):
    response = client.get("/prototype/static/styles.css")

    assert response.status_code == 200
    assert "explain-warning" in response.text
    assert "overview-card" in response.text
