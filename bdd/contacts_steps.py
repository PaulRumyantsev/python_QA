from pytest_bdd import given, when, then
from model.contacts import Contacts
import random


@given('a contact list')
def contact_list(db):
    return db.get_contacts_list()


@given('a contact with <firstname>, <lastname>, <id> and <address>')
def new_contact(firstname, lastname, id, address):
    return Contacts(firstname=firstname, lastname=lastname, id=id, address=address)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contacts.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, app, contact_list, new_contact):
    old_contacts = contact_list
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = db.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contacts_list()) == 0:
        app.contacts.create(Contacts(firstname="some name"))
    return db.get_contacts_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contacts.delete_contacts_by_id(random_contact.id)


@then('the new list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)


@when('I modify the contact from the list')
def modify_group(app, random_contact):
    app.contacts.modif_contact_by_id(id, random_contact)


@then('the new list is equal to the old list')
def verify_group_modify(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.id = random_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contacts_list(),
                                                                      key=Contacts.id_or_max)
