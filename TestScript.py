__author__ = 'Asus'
import unittest
from LoginPage import LoginPage
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SimplisticTest(unittest.TestCase):
    def test(self):
        self.assertTrue(True)

#задали формат записи лога
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)

driver = webdriver.Chrome()
driver.get("http://fix-inside.tensor.ru")
time.sleep(5)
assert "Вход в систему/СБИС" in driver.title
logging.info("Loaded main page. Logining...")
LogPage = LoginPage(driver)
LogPage.getLoginField().send_keys("check_rigth_user")
LogPage.getPasswordInput().send_keys("qwerty12")
LogPage.getloginButton().click()

time.sleep(5) #wait for next page load
logging.info("Login process started")
assert "СБИС" in driver.title

logging.info ("Login was successfull")
driver.close()

if __name__ == '__main__':
    unittest.main()