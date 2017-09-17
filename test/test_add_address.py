# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app):
        app.session.login(username="admin", password="secret")
        app.contacts.create(Address(firstname="test", middlename="test", lastname="test", title="test", nickname="test", company="test", home="test", email="test", address="test"))
        app.session.logout()


def test_add_empty_address(app):
        app.session.login(username="admin", password="secret")
        app.contacts.create(Address(firstname="", middlename="", lastname="", title="", nickname="", company="", home="", email="", address=""))
        app.session.logout()



