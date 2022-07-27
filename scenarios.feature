Feature: logging in to Swag Labs merch website

  Scenario: successful login
    Given we are on the login page
    When we fill account info for standard user
    And we click the login button
    Then we are redirected to Sauce Demo main page
    And we verify the app logo exists

  Scenario: blocked login
    Given we are on the login page
    When we fill account info for blocked user
    And we click the login button
    Then we verify the error message reads "Sorry, this user has been banned."
