import time

from Locators import pageobject


class ShopItems():

    def Shop(self,driver):
        objshop = pageobject(driver)
        shop = objshop.getshop()
        shop.click()


    def card(self,driver,phone):
        obj_carditems = pageobject(driver)
        phoneList = obj_carditems.getcarditems()

        for phones in phoneList:
            phoneName = phones.find_element_by_xpath("//div/h4/a").text
            if phoneName == phone:
                driver.find_element_by_xpath("//app-card[@class='col-lg-3 col-md-6 mb-3']/div/div/button").click()












