from model.contacts import Contacts
import random
import string


constant = [
    Contacts(firstname="firstname1", lastname="lastname1", address="address1", email="email1"),
    Contacts(firstname="firstname2", lastname="lastname2", address="address2", email2="email12")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contacts(firstname="", lastname="", address="")] + [
    Contacts(firstname=random_string("firstname", 5), lastname=random_string("lastname", 5),
             address=random_string("address", 5))
    for i in range(5)
]
