from model.contacts import Contacts
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = db.get_contacts_list()
    contacts = random.choice(old_contacts)
    app.contacts.delete_contacts_by_id(contacts.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)
