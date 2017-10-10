import re

from model.contacts import Contacts


def test_phones_on_home_page(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    contact_from_home_page = app.contacts.get_contacts_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_on_home_page(contact_from_edit_page)

#def test_emails_on_home_page(app):
    #if app.contacts.count() == 0:
        #app.contacts.create(Contacts(firstname="test"))
    #contact_from_home_page = app.contacts.get_contacts_list()[0]
    #contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    #assert contact_from_home_page.all_emails_from_home_page == merge_emails_on_home_page(contact_from_edit_page)

#def test_phones_on_contacts_view_page(app):
    #contacts_from_view_page = app.contacts.get_contacts_from_view_page(0)
    #contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    #assert contacts_from_view_page.homephone == contacts_from_edit_page.homephone
    #assert contacts_from_view_page.workphone == contacts_from_edit_page.workphone
    #assert contacts_from_view_page.mobilephone == contacts_from_edit_page.mobilephone
    #assert contacts_from_view_page.fax == contacts_from_edit_page.fax
    #assert contacts_from_view_page.secondaryphone == contacts_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -],", "", s)


def merge_phones_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contacts.homephone, contacts.mobilephone,
                                        contacts.workphone, contacts.secondaryphone]))))


def merge_emails_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contacts.email, contacts.email2, contacts.email3]))))