from model.contacts import Contacts


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
        #self.app.open_home_page()
        self.open_contact_creation_page()
        self.fill_contact_form(address)
        # submit address creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def fill_contact_form(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.firstname)
        self.change_field_value("middlename", address.middlename)
        self.change_field_value("lastname", address.lastname)
        self.change_field_value("title", address.title)
        self.change_field_value("nickname", address.nickname)
        self.change_field_value("company", address.company)
        self.change_field_value("home", address.home)
        self.change_field_value("email", address.email)
        self.change_field_value("address2", address.address)

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
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modif_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            firstname = cells[2].text
            lastname = cells[1].text
            contact_id = element.find_element_by_tag_name("input").get_attribute("id")
            contacts.append(Contacts(id=contact_id, firstname=firstname, lastname=lastname))
        return contacts

