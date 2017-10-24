from model.contacts import Contacts
import random


def test_modif_first_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = db.get_contacts_list()
    contacts = Contacts(firstname="test1")
    contacts.id = random.choice(old_contacts).id
    app.contacts.modif_contact_by_id(id, contacts)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.id = contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)
