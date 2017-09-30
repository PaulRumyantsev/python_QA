from model.contacts import Contacts


def test_modif_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    app.contacts.modif_first_contact(Contacts(firstname="test1"))

