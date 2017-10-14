# -*- coding: utf-8 -*-
from model.contacts import Contacts
import pytest
from data.add_contacts import constant as testdata


@pytest.mark.parametrize("contacts", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contacts):
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.create(contacts)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)




