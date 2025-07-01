# tests/test_service_ticket.py

def test_create_ticket(client):
    resp = client.post("/service-tickets/", json={
        "description": "Fix brakes"
    })
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["description"] == "Fix brakes"
    assert data["is_open"] is True

def test_get_tickets(client):
    from app import db
    from app.models import ServiceTicket

    ticket = ServiceTicket(description="Test ticket")
    db.session.add(ticket)
    db.session.commit()

    resp = client.get("/service-tickets/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert data[0]["description"] == "Test ticket"

def test_assign_and_remove_mechanic(client):
    from app import db
    from app.models import Mechanic, ServiceTicket

    mech = Mechanic(name="Tech", specialty="Engine")
    ticket = ServiceTicket(description="Issue")
    db.session.add_all([mech, ticket])
    db.session.commit()

    # assign
    resp = client.put(f"/service-tickets/{ticket.id}/assign-mechanic/{mech.id}")
    assert resp.status_code == 200
    data = resp.get_json()
    assert any(m["id"] == mech.id for m in data.get("mechanics", []))

    # remove
    resp = client.put(f"/service-tickets/{ticket.id}/remove-mechanic/{mech.id}")
    assert resp.status_code == 200
    data = resp.get_json()
    assert all(m["id"] != mech.id for m in data.get("mechanics", []))
