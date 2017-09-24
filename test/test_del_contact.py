from model.address import Address


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Address(firstname="test"))
    app.contacts.delete_first_contact()
