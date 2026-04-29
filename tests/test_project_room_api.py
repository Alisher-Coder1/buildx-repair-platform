def create_project(client):
    response = client.post("/api/v1/projects", json={"project_name": "Apartment Renovation"})
    assert response.status_code == 200
    return response.json()["data"]["project_id"]


def test_create_project(client):
    response = client.post("/api/v1/projects", json={"project_name": "Apartment Renovation"})

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["project_name"] == "Apartment Renovation"


def test_create_project_missing_name_returns_error(client):
    response = client.post("/api/v1/projects", json={})

    assert response.status_code == 422
    body = response.json()
    assert body["success"] is False
    assert body["errors"][0]["error_code"] == "ERR_REQUIRED_FIELD_MISSING"


def test_create_room(client):
    project_id = create_project(client)
    response = client.post(
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
    )

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["zone"] == "WET"


def test_create_room_invalid_dimension_returns_error(client):
    project_id = create_project(client)
    response = client.post(
        f"/api/v1/projects/{project_id}/rooms",
        json={
            "room_name": "Bathroom",
            "length_m": 0.1,
            "width_m": 3.0,
            "height_m": 2.7,
            "zone": "WET",
            "floor_covering": "COATING_FLOOR_PORCELAIN_TILE",
            "wall_covering": "COATING_WALL_CERAMIC_TILE",
            "ceiling_covering": "COATING_CEILING_WATER_BASED_PAINT",
        },
    )

    assert response.status_code == 422
    body = response.json()
    assert body["success"] is False
