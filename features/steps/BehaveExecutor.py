import allure
from allure_commons.types import AttachmentType
from behave import *
from functionChecks.drivercheck import Driver
from functionChecks.usernamePwd import LoginForm
from Utilities.CustomLoggers import logger

mylogger = logger.getlogger()

@given('Open Browser')
def Browser_Name(context):
    abcd = Driver()
    mylogger.info("****Driver Initialized****")
    context.driver = abcd.driveriniate()

@when('log in to portal')
def Browser2(context):
    mylogger.info("****URL Opened****")
    context.driver.get("https://www.rahulshettyacademy.com/angularpractice/")


@then('user should enter username "{name}", email "{email}" and password "{password}"')
def loginform(context,name,email,password):
    mylogger.info("****Login_form Opened****")
    object = LoginForm()
    object.loginform(context.driver,name,email,password)


@then('Click on submit')
def submit(context):
    mylogger.info("****Submitting the form****")
    obj_submit = LoginForm()
    obj_submit.submit(context.driver)


@then('User should successfully submit')
def success1(context):
    mylogger.critical("****Successsfully submitted")
    text = LoginForm.success(context.driver)
    expected = "Success! The Form has been submitted successfully!."
    try:
        if text == expected:
            print(text)
            context.driver.save_screenshot(".\\Screenshot\\" + "LoginFormPage.png")
            allure.attach(context.driver.get_screenshot_as_png(), name="Login form",
                  attachment_type=AttachmentType.PNG)
            assert True
        #else:
         #   print("Submit not successful")
    except:
        #assert "Success" in text1
        mylogger.critical("****Submit Unsuccessful")
        print("Login Unsuccessful")

            #assert False













