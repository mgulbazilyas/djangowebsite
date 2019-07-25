from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import os
import xlwings as xw
import pandas as pd
class Setup:
    __user = 'Hello@dhukaan.co.uk'
    __passwd = 'C5Ux8rusrx'


    def __init__(self,driver=None):
        self.book = xw.Book(input("Enter the file location: ").replace('\"', ''))
        #self.categories = self.listGet()
        if driver is not None: self.driver = driver;return
        self.driver = Chrome()
        self.driver.set_window_size(1200, 700)
        self.driver.get("https://cpp.custom-gateway.net/v2/login?return=L3YyL3Byb2R1Y3QtbWFuYWdlci9wcm9kdWN0cw==#/")
        self.login()


    '''def listGet(self):
        sht = self.book.sheets[2]
        vals = sht.range('a2').expand().value
        vals = [i[:4] for i in vals]
        return vals
    '''

    def login(self):
        userField = self.driver.find_element_by_css_selector('input#username')
        userField.clear();
        userField.send_keys(self.__user)
        passField = self.driver.find_element_by_xpath('//input[@name="password"]')
        passField.clear();
        passField.send_keys(self.__passwd)
        self.driver.find_element_by_css_selector('button.btn.btn-primary').click()
        time.sleep(3)

    def wait_element(self,by,el):
        while 1:
            try:
                print('waiting',end='\t')
                return self.driver.find_element(by,el)
                break
            except:
                time.sleep(0.5)
                pass
    def loadMaskWait(self):
        while 1:
            try:
                self.driver.find_element(By.XPATH, "//div[@class='loadmask']")
                time.sleep(1)
            except:
                break

    def check_el(self, El, Text):
        return WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element((El,Text.split(' ')[0])))

    def get_el(self, data_bind):
        return WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,f'//*[@data-bind="{data_bind}"]')))

    def wait(self, thing):
        return WebDriverWait(self.driver,20).until(thing)

