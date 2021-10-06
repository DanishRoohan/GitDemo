import time

from Locators import pageobject



class LoginForm():
    def loginform(self,driver,name,email,password):
        obj1 = pageobject(driver)
        username = obj1.getusername()
        email1 = obj1.getemail()
        password1 = obj1.getpassword()
        username.send_keys(name)
        email1.send_keys(email)
        password1.send_keys(password)

        time.sleep(3)

    def submit(self,driver):
        obj2 = pageobject(driver)
        obj2.getsubmit()
    @staticmethod
    def success(driver):
        obj3 = pageobject(driver)
        Success100 = obj3.getsuccess()
        textsuccess = Success100.text
        print(textsuccess)
        return textsuccess




# driver.find_element_by_name("name").send_keys(name)

# driver.find_element_by_id("exampleInputPassword1").send_keys(password)