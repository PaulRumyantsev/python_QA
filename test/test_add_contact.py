# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app, db, json_contacts):
    contacts = json_contacts
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.create(contacts)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)




