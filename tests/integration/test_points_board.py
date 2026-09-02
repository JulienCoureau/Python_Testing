import server

def test_points_board_is_public(client):
    """Fonctionnalite : le tableau des points est visible sans connexion"""
    response = client.get("/points")

    assert response.status_code == 200
    # On doit voir les clubs et leurs solde sur la page
    for club in server.clubs:
        assert club['name'].encode() in response.data
        assert club['points'].encode() in response.data

