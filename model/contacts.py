from sys import maxsize

class Contacts:
    def __init__(self, firstname=None, middlename=None, lastname=None, title=None, nickname=None, company=None, home=None, email=None, address=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.nickname = nickname
        self.company = company
        self.home = home
        self.email = email
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize