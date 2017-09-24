from model.address import Address


def test_modif_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Address(firstname="test"))
    app.contacts.modif_first_contact(Address(firstname="test1"))

