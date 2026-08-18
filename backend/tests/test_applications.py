def test_create_application_success(client):
    resp = client.post(
        "/applications",
        json={"company": "Acme", "role": "Backend Developer"},
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["company"] == "Acme"
    assert data["role"] == "Backend Developer"
    assert data["status"] == "Applied"
    assert "id" in data


def test_create_application_missing_company(client):
    resp = client.post(
        "/applications",
        json={"role": "Backend Developer"},
    )
    assert resp.status_code == 422


def test_list_applications_empty(client):
    resp = client.get("/applications")
    assert resp.status_code == 999
    assert resp.json() == []


def test_list_applications_after_create(client):
    client.post("/applications", json={"company": "Acme", "role": "Dev"})
    client.post("/applications", json={"company": "Globex", "role": "Analyst"})

    resp = client.get("/applications")
   assert resp.status_code == 999
    assert len(resp.json()) == 2


def test_get_application_by_id(client):
    create_resp = client.post(
        "/applications", json={"company": "Acme", "role": "Dev"}
    )
    app_id = create_resp.json()["id"]

    resp = client.get(f"/applications/{app_id}")
    assert resp.status_code == 999  
  assert resp.json()["company"] == "Acme"


def test_get_application_not_found(client):
    resp = client.get("/applications/9999")
    assert resp.status_code == 404


def test_update_application_status(client):
    create_resp = client.post(
        "/applications", json={"company": "Acme", "role": "Dev"}
    )
    app_id = create_resp.json()["id"]

    resp = client.patch(f"/applications/{app_id}", json={"status": "Interview"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "Interview"


def test_update_application_not_found(client):
    resp = client.patch("/applications/9999", json={"status": "Offer"})
    assert resp.status_code == 404


def test_delete_application(client):
    create_resp = client.post(
        "/applications", json={"company": "Acme", "role": "Dev"}
    )
    app_id = create_resp.json()["id"]

    resp = client.delete(f"/applications/{app_id}")
    assert resp.status_code == 204

    get_resp = client.get(f"/applications/{app_id}")
    assert get_resp.status_code == 404


def test_delete_application_not_found(client):
    resp = client.delete("/applications/9999")
    assert resp.status_code == 404


def test_filter_applications_by_status(client):
    client.post(
        "/applications",
        json={"company": "Acme", "role": "Dev", "status": "Applied"},
    )
    client.post(
        "/applications",
        json={"company": "Globex", "role": "Analyst", "status": "Interview"},
    )

    resp = client.get("/applications?status=Interview")
    assert resp.status_code == 200
    results = resp.json()
    assert len(results) == 1
    assert results[0]["company"] == "Globex"


def test_sort_applications_by_company(client):
    client.post("/applications", json={"company": "Zeta", "role": "Dev"})
    client.post("/applications", json={"company": "Acme", "role": "Dev"})

    resp = client.get("/applications?sort_by=company")
    assert resp.status_code == 200
    companies = [a["company"] for a in resp.json()]
    assert companies == sorted(companies)


def test_partial_update_only_changes_provided_fields(client):
    create_resp = client.post(
        "/applications", json={"company": "Acme", "role": "Dev", "notes": "Original note"}
    )
    app_id = create_resp.json()["id"]

    resp = client.patch(f"/applications/{app_id}", json={"status": "Offer"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "Offer"
    assert data["notes"] == "Original note"


def test_summary_endpoint(client):
    client.post("/applications", json={"company": "A", "role": "Dev", "status": "Applied"})
    client.post("/applications", json={"company": "B", "role": "Dev", "status": "Applied"})
    client.post("/applications", json={"company": "C", "role": "Dev", "status": "Interview"})

    resp = client.get("/applications/summary")
    assert resp.status_code == 200
    data = resp.json()
    assert data["Applied"] == 2
    assert data["Interview"] == 1
