import server
from datetime import datetime, timedelta

def test_full_booking_journey(client):
    """Parcour complet : connexion, reservation, achat, deconnexion"""
    competition = next(
        c for c in server.competitions if c['name'] == "Spring Festival"
    )
    competition['date'] = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")

    # Connexion
    response = client.post("/showSummary", data={"email":"john@simplylift.co"})
    assert b"Spring Festival" in response.data

    # Page de reservation
    response = client.get("/book/Spring Festival/Simply Lift")
    assert response.status_code == 200

    # Achat de place
    response = client.post(
        "/purchasePlaces",
        data={"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
    )
    assert b"Great-booking complete!" in response.data
    assert b"Points available: 11" in response.data  # 13 - 2

    # Deconnexion
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200