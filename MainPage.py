__author__ = 'Asus'
class MainPage:
    def __init__(self, driver, staffLink='div[data-id="staff"] > a'):
        self.driver = driver
        self.staffLink = staffLink

    def getstaffLink(self):
        return self.driver.find_element_by_css_selector(self.staffLink)

    def getClosePopupLinks(self):
        locator = "a.ws-window-titlebar-action.close"
        return self.driver.find_elements_by_css_selector(locator)
