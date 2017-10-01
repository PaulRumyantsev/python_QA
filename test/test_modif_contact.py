from model.contacts import Contacts


def test_modif_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = app.contacts.get_contacts_list()
    contacts = Contacts(firstname="test1")
    contacts.id = old_contacts[0].id
    app.contacts.modif_first_contact(contacts)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

