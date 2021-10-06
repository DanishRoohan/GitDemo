
from behave import *
from functionChecks.shopitems import ShopItems


@then('Click on shop')
def shop(context):
    object2 = ShopItems()
    object2.Shop(context.driver)

@then('User should select an item from the card "{phone}"')
def carditems(context,phone):
    obj_carditems = ShopItems()
    obj_carditems.card(context.driver,phone)
    context.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

