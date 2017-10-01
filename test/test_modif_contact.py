from model.contacts import Contacts
from random import randrange


def test_modif_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    contacts = Contacts(firstname="test1")
    contacts.id = old_contacts[index].id
    app.contacts.modif_contact_by_index(index, contacts)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
