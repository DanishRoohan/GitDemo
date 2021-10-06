
Feature: Web Page form

  Background: common steps
    Given Open Browser
    When log in to portal
  @critical
  Scenario Outline: Register form for login

    Then user should enter username "<username>", email "<email>" and password "<password>"
    And Click on submit
    And User should successfully submit
    #And Click on shop

    Examples:
      | username |email       |password|
      |danish    |danish@mail |123 |
      #|sufi      |sufi@gmail  |456  |

  @trivial
  Scenario Outline: Shopping page
    Then Click on shop
    And User should select an item from the card "<phone>"


    #Then User should select "<phone>"
    #And User should add in cart
    #And User should checkout
    Examples:
      |phone |
      |iphone X|