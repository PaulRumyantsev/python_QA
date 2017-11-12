# -*- coding: utf-8 -*-
from model.contacts import Contacts
import pytest


def test_add_contact(app, db, json_contacts):
    contacts = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contacts_list()
    with pytest.allure.step('When I add the contact to the list'):
        app.contacts.create(contacts)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        assert len(old_contacts) + 1 == app.contacts.count()
        new_contacts = db.get_contacts_list()
        old_contacts.append(contacts)
        assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)




