import mysql.connector
from model.group import Group
from model.contacts import Contacts


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                id = row[0]
                name = row[1]
                header = row[2]
                footer = row[3]
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, work, mobile, phone2, address, email, email2, email3 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor.fetchall():
                (id, firstname, lastname, homephone, workphone, mobilephone,
                 secondaryphone, address, email, email2, email3) = row
                list.append(Contacts(id=str(id), firstname=firstname, lastname=lastname, homephone=homephone,
                                     workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone,
                                     address=address, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
