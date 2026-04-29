def test_core_summary_returns_expected_geometry(client):
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
    response = client.get(f"/api/v1/rooms/{room_id}/core-summary")

    assert response.status_code == 200
    body = response.json()
    geometry = body["data"]["geometry"]

    assert geometry["floor_area_m2"] == 12.0
    assert geometry["ceiling_area_m2"] == 12.0
    assert geometry["perimeter_m"] == 14.0
    assert geometry["wall_area_m2"] == 37.8
