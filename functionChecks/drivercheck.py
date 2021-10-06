
from selenium import webdriver




class Driver:
    def driveriniate(self):
        driver = webdriver.Chrome(executable_path="c://chromedriver.exe")
        return driver




        #browser_name = ""
        #if browser_name == "chrome":
         #   driver = webdriver.Chrome(executable_path="c://chromedriver.exe")
        #elif browser_name == "msedge":
         #   driver = webdriver.Edge(executable_path="c://msedgedriver.exe")
        #return driver

