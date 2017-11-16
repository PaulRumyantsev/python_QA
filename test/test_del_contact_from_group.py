from fixture.orm import ORMFixture
from model.group import Group
from model.contacts import Contacts

import random

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_delete_contact_from_group(app):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_contacts = db.get_contacts_list()
    old_groups = db.get_group_list()
    contacts = random.choice(old_contacts)
    group = random.choice(old_groups)
    old_contacts_in_group = db.get_contacts_in_group(group)
    if len(db.get_contacts_in_group(group)) == 0:
        app.contacts.add_contacts_to_group(contacts, group)
    else:
        contacts = random.choice(old_contacts_in_group)
    old_contacts_in_group_update = db.get_contacts_in_group(group)
    app.contacts.delete_contacts_from_group(contacts, group)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group_update) - 1 == len(new_contacts_in_group)
    old_contacts_in_group_update.remove(contacts)
    assert sorted(old_contacts_in_group_update, key=Contacts.id_or_max) == sorted(new_contacts_in_group,
                                                                                 key=Contacts.id_or_max)