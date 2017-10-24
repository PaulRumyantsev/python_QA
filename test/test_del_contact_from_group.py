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
    contacts_id = random.choice(old_contacts).id
    group_id = random.choice(old_groups).id
    if len(db.get_contacts_in_group(Group(id='%s' % group_id))) == 0:
        app.contacts.add_contacts_to_group(contacts_id, group_id)
    old_contacts_in_group = db.get_contacts_in_group(Group(id='%s' % group_id))
    app.contacts.delete_contacts_from_group(group_id)
    new_contacts_in_group = db.get_contacts_in_group(Group(id='%s' % group_id))
    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)