__author__ = 'Asus'
# поскольку изначально у меня всегда изначально отображается ссылка "Наша компания", выбираем пункт "Все юридические лица"
class StaffPage:
    def __init__(self, driver, orgLink = "#ourOrg", orgForm = "div[title='Выберите организацию']", changeOrg = "div[title='Все юридические лица']"):
        self.driver = driver
        self.orgLink = orgLink
        self.orgForm  = orgForm
        self.changeOrg = changeOrg

    def getorgLink(self):
        return self.driver.find_element_by_css_selector(self.orgLink)

    def getorgForm(self):
        return self.driver.find_element_by_css_selector(self.orgForm)

    def isOrgFormVisible(self):
        return len(self.driver.find_elements_by_css_selector(self.orgForm)) > 0

    def getchangeOrg(self):
        return self.driver.find_element_by_css_selector(self.changeOrg)
