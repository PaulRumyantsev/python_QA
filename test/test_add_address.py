# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_address(app):
        #old_contacts = app.contacts.get_contacts_list()
        app.contacts.create(Contacts(firstname="test", middlename="test", lastname="test", title="test", nickname="test", company="test", home="test", email="test", address="test"))
        #new_contacts = app.contacts.get_contacts_list()
        #assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_address(app):
        app.contacts.create(Contacts(firstname="", middlename="", lastname="", title="", nickname="", company="", home="", email="", address=""))




