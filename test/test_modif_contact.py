

def test_modif_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.modif_first_contact()
    app.session.logout()