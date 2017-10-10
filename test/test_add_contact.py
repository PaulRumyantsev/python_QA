# -*- coding: utf-8 -*-
from model.contacts import Contacts
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contacts(firstname="", lastname="", address="")] + [
    Contacts(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5),
             address=random_string("address", 5))
    for i in range(5)
]


@pytest.mark.parametrize("contacts", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contacts):
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.create(contacts)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)




