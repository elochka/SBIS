__author__ = 'Asus'
# поскольку изначально у меня всегда отображается ссылка "Наша компания", выбираем для проверки пункт "Все юридические лица"
class StaffPage:
    def __init__(self, driver, orgLink = "#ourOrg", orgForm = "div[title='Выберите организацию']", changeOrg = "div[title='Все юридические лица']", searchField = "#fld-searchStaff", employeeResult = "div[class='listEmplInfoBlock ']"):
        self.driver = driver
        self.orgLink = orgLink
        self.orgForm  = orgForm
        self.changeOrg = changeOrg
        self.searchField = searchField
        self.employeeResult = employeeResult

    def getorgLink(self):
        return self.driver.find_element_by_css_selector(self.orgLink)

    def getorgForm(self):
        return self.driver.find_element_by_css_selector(self.orgForm)

    def isOrgFormVisible(self):
        return len(self.driver.find_elements_by_css_selector(self.orgForm)) > 0

    def getchangeOrg(self):
        return self.driver.find_element_by_css_selector(self.changeOrg)

    def getemployeeResult(self):
        return self.driver.find_element_by_css_selector(self.employeeResult)

    def getsearchField(self):
        return self.driver.find_element_by_css_selector(self.searchField)
