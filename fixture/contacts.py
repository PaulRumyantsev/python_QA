from model.contacts import Contacts
import re
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, address):
        wd = self.app.wd
        # self.app.open_home_page()
        self.open_contact_creation_page()
        self.fill_contact_form(address)
        # submit address creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def fill_contact_form(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.firstname)
        self.change_field_value("middlename", address.middlename)
        self.change_field_value("lastname", address.lastname)
        self.change_field_value("title", address.title)
        self.change_field_value("nickname", address.nickname)
        self.change_field_value("company", address.company)
        self.change_field_value("address", address.address)
        self.change_field_value("home", address.homephone)
        self.change_field_value("mobile", address.mobilephone)
        self.change_field_value("work", address.workphone)
        self.change_field_value("fax", address.fax)
        self.change_field_value("email", address.email)
        self.change_field_value("phone2", address.secondaryphone)

    def change_field_value(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def open_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # delete contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def delete_contacts_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # delete contact
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modif_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.select_modif_contact_by_index(index)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def modif_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        self.select_modif_contact_by_id(id)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def select_modif_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def select_modif_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def modif_first_contact(self):
        self.modif_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contacts_cache.append(Contacts(firstname=firstname, lastname=lastname, id=id, address=address,
                                                    all_phones_from_home_page=all_phones,
                                                    all_emails_from_home_page=all_emails))
        return list(self.contacts_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contacts(firstname=firstname, lastname=lastname, id=id,
                        homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                        secondaryphone=secondaryphone, address=address, email=email, email2=email2, email3=email3)

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contacts(homephone=homephone, workphone=workphone, mobilephone=mobilephone, fax=fax,
                        secondaryphone=secondaryphone)

    def add_contacts_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()
        select = Select(wd.find_element_by_css_selector("select[name='to_group']"))
        select.select_by_value('%s' % group.id)
        wd.find_element_by_css_selector("input[value='Add to']").click()
        wd.find_element_by_css_selector("a[href='./?group=%s']" % group.id).click()

    def delete_contacts_from_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        select = Select(wd.find_element_by_css_selector("select[name='group']"))
        select.select_by_value('%s' % group.id)
        wd.find_element_by_css_selector("input[id='%s']" % contact.id).click()
        wd.find_element_by_css_selector("input[name='remove']").click()
        wd.find_element_by_css_selector("a[href='./?group=%s']" % group.id).click()

