__author__ = 'Asus'
class StaffPage:
    def __init__(self, driver, orgLink="#ourOrg"):
        self.driver = driver
        self.orgLink = orgLink
    def getorgLink(self):
        return self.driver.find_element_by_css_selector(self.orgLink)
