from selenium import webdriver
from selenium.webdriver.common.by import By


class pageobject:
    def __init__(self,driver):
        self.driver = driver

    username = (By.NAME, "name")
    password = (By.ID, "exampleInputPassword1")
    email = (By.NAME, "email")
    shop = (By.LINK_TEXT, "Shop")
    submit = (By.XPATH, "//input[@type='submit']")
    success= (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    carditems = (By.XPATH, "//app-card[@class='col-lg-3 col-md-6 mb-3']/div")


    def getusername(self):
        return self.driver.find_element(*pageobject.username)


    def getpassword(self):
        return self.driver.find_element(*pageobject.password)

    def getemail(self):
        return self.driver.find_element(*pageobject.email)

    def getshop(self):
        return self.driver.find_element(*pageobject.shop)

    def getsubmit(self):
        return self.driver.find_element(*pageobject.submit).click()

    def getsuccess(self):
        return self.driver.find_element(*pageobject.success)

    def getcarditems(self):
        return self.driver.find_elements(*pageobject.carditems)

