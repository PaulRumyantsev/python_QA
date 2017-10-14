from model.contacts import Contacts
import random
import string
import os.path
import json



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contacts(firstname="", lastname="", address="")] + [
    Contacts(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5),
             address=random_string("address", 5))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))