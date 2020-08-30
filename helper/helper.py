import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Helper(object):

    driver = webdriver.Chrome(executable_path='D:\Python\BDD_DW\chromedriver.exe')
    driver.implicitly_wait(10)
    url = "http://www.way2automation.com/angularjs-protractor/banking/#/login"

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def screenshot(self,name):
        screenshot_name = name + ".png"
        self.driver.save_screenshot(screenshot_name)
        path = os.getcwd()
        print("Screenshot captured :" + path + screenshot_name)