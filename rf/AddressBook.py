import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group
from model.contacts import Contacts


class AddressBook:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target("--target")['web']
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                                   password=db_config['password'])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def new_contact(self, firstname, lastname, id, address):
        return Contacts(firstname=firstname, lastname=lastname, id=id, address=address)

    def get_contact_list(self):
        return self.dbfixture.get_contacts_list()

    def create_contact(self, contact):
        self.fixture.contacts.create(contact)

    def delete_contact(self, contact):
        self.fixture.contacts.delete_contacts_by_id(contact.id)

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contacts.id_or_max) == sorted(list2, key=Contacts.id_or_max)

    def modify_contact(self, contact):
        self.fixture.contacts.modif_contacts_by_id(contact.id)