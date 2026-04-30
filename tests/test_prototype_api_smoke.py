def test_full_backend_prototype_api_smoke_path(client):
    health = client.get("/api/v1/health")
    assert health.status_code == 200
    assert health.json()["success"] is True

    project_response = client.post(
        "/api/v1/projects",
        json={"project_name": "Prototype Smoke Test Project"},
    )
    assert project_response.status_code == 200
    project_body = project_response.json()
    assert project_body["success"] is True

    project_id = project_body["data"]["project_id"]

    room_payload = {
        "room_name": "Bathroom",
        "length_m": 4.0,
        "width_m": 3.0,
        "height_m": 2.7,
        "zone": "WET",
        "floor_covering": "COATING_FLOOR_PORCELAIN_TILE",
        "wall_covering": "COATING_WALL_CERAMIC_TILE",
        "ceiling_covering": "COATING_CEILING_WATER_BASED_PAINT",
    }

    room_response = client.post(
        f"/api/v1/projects/{project_id}/rooms",
        json=room_payload,
    )
    assert room_response.status_code == 200
    room_body = room_response.json()
    assert room_body["success"] is True

    room_id = room_body["data"]["room_id"]

    project_read = client.get(f"/api/v1/projects/{project_id}")
    assert project_read.status_code == 200
    assert project_read.json()["success"] is True

    room_read = client.get(f"/api/v1/rooms/{room_id}")
    assert room_read.status_code == 200
    assert room_read.json()["success"] is True

    core_summary = client.get(f"/api/v1/rooms/{room_id}/core-summary")
    assert core_summary.status_code == 200
    core_data = core_summary.json()["data"]
    assert core_data["geometry"]["floor_area_m2"] == 12.0
    assert core_data["geometry"]["ceiling_area_m2"] == 12.0
    assert core_data["geometry"]["perimeter_m"] == 14.0
    assert core_data["geometry"]["wall_area_m2"] == 37.8

    execution_summary = client.get(f"/api/v1/rooms/{room_id}/execution-summary")
    assert execution_summary.status_code == 200
    execution_data = execution_summary.json()["data"]
    execution_operation_ids = [item["operation_id"] for item in execution_data["operations"]]
    assert "OPR_FLOOR_WATERPROOFING" in execution_operation_ids
    assert "OPR_WALL_WATERPROOFING" in execution_operation_ids
    assert "OPR_FLOOR_TILE_INSTALL" in execution_operation_ids
    assert "OPR_WALL_TILE_INSTALL" in execution_operation_ids

    material_summary = client.get(f"/api/v1/rooms/{room_id}/material-consumption-summary")
    assert material_summary.status_code == 200
    material_data = material_summary.json()["data"]
    material_ids = [item["material_id"] for item in material_data["items"]]
    assert "MAT_PORCELAIN_TILE" in material_ids
    assert "MAT_TILE_ADHESIVE" in material_ids
    assert "MAT_GROUT" in material_ids

    cost_summary = client.get(f"/api/v1/rooms/{room_id}/cost-summary")
    assert cost_summary.status_code == 200
    cost_body = cost_summary.json()
    assert cost_body["success"] is True
    assert cost_body["warnings"][0]["error_code"] == "MISSING_PRICE"
    assert cost_body["data"]["grand_total"] is None

    procurement_summary = client.get(f"/api/v1/rooms/{room_id}/procurement-summary")
    assert procurement_summary.status_code == 200
    procurement_body = procurement_summary.json()
    assert procurement_body["success"] is True
    assert procurement_body["data"]["room_id"] == room_id
    assert len(procurement_body["data"]["items"]) > 0

    first_procurement_item = procurement_body["data"]["items"][0]
    assert "material_id" in first_procurement_item
    assert "package_count" in first_procurement_item
    assert "purchase_quantity" in first_procurement_item
