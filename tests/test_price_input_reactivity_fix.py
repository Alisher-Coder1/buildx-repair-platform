def test_frontend_js_updates_price_views_without_full_cost_rerender(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert "updatePriceDerivedViews" in response.text
    assert "data-price-total" in response.text
    assert "data-price-status" in response.text
    assert 'document.querySelector("#costTotal")' in response.text


def test_frontend_js_updates_procurement_status_after_price_input(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert "renderProcurement(lastProcurementData.data)" in response.text
    assert "пересчитает стоимость материалов, общий итог и статус закупки" in response.text


def test_frontend_js_does_not_rerender_cost_table_on_each_input(client):
    response = client.get("/prototype/static/app.js")

    assert response.status_code == 200
    assert 'input.addEventListener("input", () => {' in response.text
    assert "updatePriceDerivedViews();" in response.text
