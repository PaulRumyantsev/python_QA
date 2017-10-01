from model.contacts import Contacts


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.delete_first_contact()
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)