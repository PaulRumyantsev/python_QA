from sys import maxsize


class Contacts:
    def __init__(self, firstname=None, middlename=None, lastname=None, title=None, nickname=None, company=None,
                 home=None, email=None, email2=None, email3=None, address=None, homephone=None, mobilephone=None, workphone=None, fax=None,
                 id=None, secondaryphone=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.nickname = nickname
        self.company = company
        self.home = home
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize