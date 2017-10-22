from datetime import datetime
from pony.orm import *
from model.group import Group
from model.contacts import Contacts
from pymysql.converters import decoders


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContacts(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column="deprecated")

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    def get_group_list(self):
        with db_session:
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contacts):
            return Contacts(id=str(contacts.id), firstname=contacts.firstname, lastname=contacts.lastname)

        return list(map(convert, contacts))

    def get_contacts_list(self):
        with db_session:
            return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContacts if c.deprecated is None))
