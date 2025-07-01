def test_create_mechanic(client):
    resp = client.post("/mechanics/", json={
        "name": "Bob",
        "specialty": "Engine"
    })
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "Bob"
    assert data["specialty"] == "Engine"

def test_get_mechanics(client):
    from app import db
    from app.models import Mechanic

    # seed one mechanic (this is inside app_context now)
    mech = Mechanic(name="Alice", specialty="Brakes")
    db.session.add(mech)
    db.session.commit()

    resp = client.get("/mechanics/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert data[0]["name"] == "Alice"
    assert data[0]["specialty"] == "Brakes"

def test_update_mechanic(client):
    from app import db
    from app.models import Mechanic

    mech = Mechanic(name="Carl", specialty="Tires")
    db.session.add(mech)
    db.session.commit()

    resp = client.put(f"/mechanics/{mech.id}", json={
        "name": "Carl Updated"
    })
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["name"] == "Carl Updated"

def test_delete_mechanic(client):
    from app import db
    from app.models import Mechanic

    mech = Mechanic(name="Dana", specialty="Battery")
    db.session.add(mech)
    db.session.commit()

    resp = client.delete(f"/mechanics/{mech.id}")
    assert resp.status_code == 204
    assert Mechanic.query.get(mech.id) is None
