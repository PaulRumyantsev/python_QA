# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app):
        old_contacts = app.contacts.get_contacts_list()
        contacts = Contacts(firstname="test", middlename="test", lastname="test", title="test", nickname="test", company="test", home="test", email="test", address="test")
        app.contacts.create(contacts)
        new_contacts = app.contacts.get_contacts_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contacts)
        assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


def test_add_empty_contact(app):
        old_contacts = app.contacts.get_contacts_list()
        contacts = Contacts(firstname="", middlename="", lastname="", title="", nickname="", company="", home="", email="", address="")
        app.contacts.create(contacts)
        new_contacts = app.contacts.get_contacts_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contacts)
        assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)



