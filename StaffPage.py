__author__ = 'Asus'
class StaffPage:
    def __init__(self, driver, orgLink="#ourOrg", orgForm = "#div_WKW19MzcNgg"):
        self.driver = driver
        self.orgLink = orgLink
        self.orgForm  = orgForm

    def getorgLink(self):
        return self.driver.find_element_by_css_selector(self.orgLink)

    def getorgForm(self):
        return self.driver.find_element_by_css_selector(self.getorgForm())
