import server

def test_book_page_displays_competition(client):
    """La page de reservation affiche la competition et le club choisis"""
    response = client.get("/book/Spring Festival/Simply Lift")

    assert response.status_code == 200
    assert b"Spring Festival" in response.data

def test_logout_redirects_to_index(client):
    """Deconnexion ramene a la page d'acceuil"""
    response = client.get("/logout", follow_redirects=True)

    assert response.status_code == 200
    assert b"GUDLFT Registration" in response.data