# -*- coding: utf-8 -*-
from model.address import Address


def test_add_address(app):
        app.contacts.create(Address(firstname="test", middlename="test", lastname="test", title="test", nickname="test", company="test", home="test", email="test", address="test"))


def test_add_empty_address(app):
        app.contacts.create(Address(firstname="", middlename="", lastname="", title="", nickname="", company="", home="", email="", address=""))




