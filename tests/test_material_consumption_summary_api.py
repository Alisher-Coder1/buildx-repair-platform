def test_material_consumption_summary_endpoint(client):
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

    room_id = room["data"]["room_id"]
    response = client.get(f"/api/v1/rooms/{room_id}/material-consumption-summary")

    assert response.status_code == 200
    body = response.json()

    assert body["success"] is True
    assert body["data"]["room_id"] == room_id
    assert body["data"]["artifact_version"] == "v1"

    material_ids = [item["material_id"] for item in body["data"]["items"]]
    assert "MAT_PORCELAIN_TILE" in material_ids
    assert "MAT_TILE_ADHESIVE" in material_ids
    assert "MAT_GROUT" in material_ids


def test_material_consumption_summary_room_not_found(client):
    response = client.get("/api/v1/rooms/not-existing-room/material-consumption-summary")

    assert response.status_code == 404
    body = response.json()["detail"]
    assert body["success"] is False
    assert body["errors"][0]["error_code"] == "ERR_NOT_FOUND"
