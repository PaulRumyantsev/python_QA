from model.contacts import Contacts


def test_modif_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.modif_first_contact(Contacts(firstname="test1"))
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
