import mysql.connector
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contacts_list()
    for contacts in contacts:
        print(contacts)
    print(len(contacts))
finally:
    db.destroy()
