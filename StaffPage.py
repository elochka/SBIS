__author__ = 'Asus'
class StaffPage:
    def __init__(self, driver, orgLink="#ourOrg", orgForm = "div[title='Выберите организацию']"):
        self.driver = driver
        self.orgLink = orgLink
        self.orgForm  = orgForm

    def getorgLink(self):
        return self.driver.find_element_by_css_selector(self.orgLink)

    def getorgForm(self):
        return self.driver.find_element_by_css_selector(self.orgForm)

    def isOrgFormVisible(self):
        return len(self.driver.find_elements_by_css_selector(self.orgForm)) > 0
