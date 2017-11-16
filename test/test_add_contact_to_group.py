from fixture.orm import ORMFixture
from model.group import Group
from model.contacts import Contacts
import pytest
import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact_to_group(app):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_contacts = db.get_contacts_list()
    old_groups = db.get_group_list()
    contact = random.choice(old_contacts)
    group = random.choice(old_groups)
    old_contacts_in_group = db.get_contacts_in_group(group)
    if len(db.get_contacts_list()) == len(old_contacts_in_group):
        app.contact.create(Contacts(firstname="test"))
    app.contacts.add_contacts_to_group(contact, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contacts.id_or_max) == sorted(new_contacts_in_group, key=Contacts.id_or_max)







