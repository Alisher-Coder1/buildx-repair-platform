def test_prototype_frontend_page_available(client):
    response = client.get("/prototype")

    assert response.status_code == 200
    assert "Buildx Repair Platform" in response.text
    assert "Prototype Room Flow" in response.text


def test_prototype_frontend_static_js_available(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert "material-consumption-summary" in response.text
    assert "procurement-summary" in response.text


def test_prototype_frontend_static_css_available(client):
    response = client.get("/prototype/static/styles.css")

    assert response.status_code == 200
    assert "app-shell" in response.text
