def create_wet_tile_room(client):
    project = client.post("/api/v1/projects", json={"project_name": "Apartment Renovation"}).json()
    project_id = project["data"]["project_id"]

    room = client.post(
        f"/api/v1/projects/{project_id}/rooms",
        json={
            "room_name": "Bathroom",
            "length_m": 4.0,
            "width_m": 3.0,
            "height_m": 2.7,
            "zone": "WET",
            "floor_covering": "COATING_FLOOR_PORCELAIN_TILE",
            "wall_covering": "COATING_WALL_CERAMIC_TILE",
            "ceiling_covering": "COATING_CEILING_WATER_BASED_PAINT",
        },
    ).json()

    return room["data"]["room_id"]


def test_cost_summary_endpoint(client):
    room_id = create_wet_tile_room(client)

    response = client.get(f"/api/v1/rooms/{room_id}/cost-summary")

    assert response.status_code == 200
    body = response.json()

    assert body["success"] is True
    assert body["data"]["room_id"] == room_id
    assert body["data"]["currency"] == "USD"
    assert body["data"]["grand_total"] is None
    assert body["warnings"][0]["error_code"] == "MISSING_PRICE"


def test_procurement_summary_endpoint(client):
    room_id = create_wet_tile_room(client)

    response = client.get(f"/api/v1/rooms/{room_id}/procurement-summary")

    assert response.status_code == 200
    body = response.json()

    assert body["success"] is True
    assert body["data"]["room_id"] == room_id
    assert body["data"]["currency"] == "USD"

    item = body["data"]["items"][0]
    assert "material_id" in item
    assert "package_count" in item
    assert "purchase_quantity" in item


def test_cost_summary_room_not_found(client):
    response = client.get("/api/v1/rooms/not-existing-room/cost-summary")

    assert response.status_code == 404
    body = response.json()["detail"]
    assert body["success"] is False
    assert body["errors"][0]["error_code"] == "ERR_NOT_FOUND"


def test_procurement_summary_room_not_found(client):
    response = client.get("/api/v1/rooms/not-existing-room/procurement-summary")

    assert response.status_code == 404
    body = response.json()["detail"]
    assert body["success"] is False
    assert body["errors"][0]["error_code"] == "ERR_NOT_FOUND"
