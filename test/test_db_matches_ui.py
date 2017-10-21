from model.group import Group
from model.contacts import Contacts


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contacts_list(app, db):
    ui_list = app.contacts.get_contacts_list()

    def clean(contacts):
        return Contacts(id=contacts.id, firstname=contacts.firstname.strip())

    db_list = map(clean, db.get_contacts_list())
    assert sorted(ui_list, key=Contacts.id_or_max) == sorted(db_list, key=Contacts.id_or_max)
