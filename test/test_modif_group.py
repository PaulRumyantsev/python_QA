

def test_modif_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modif_first_group()
    app.session.logout()