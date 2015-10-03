__author__ = 'Asus'
class LoginPage:
    def __init__(self, driver, loginField="#fld-loginName", passwordField="#fld-loginPass", loginButton="#logButton"):
        self.driver = driver
        self.loginField = loginField
        self.passwordField = passwordField
        self.loginButton = loginButton

    def getLoginField(self):
        return self.driver.find_element_by_css_selector(self.loginField)

    def getPasswordInput(self):
        return self.driver.find_element_by_css_selector(self.passwordField)

    def getloginButton(self):
        return self.driver.find_element_by_css_selector(self.loginButton)


