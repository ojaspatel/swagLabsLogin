from behave import *
import sys
sys.path.append('../')
import test_functions

test = test_functions.Test()
test.start_session()

@given('we are on the login page')
def step_impl(context):
    test.login_page.load_page()
    test.driver.implicitly_wait(5)
    assert test.driver.current_url == "https://www.saucedemo.com/"

@when('we fill account info for standard user')
def step_impl(context):
    test.login_page.fill_standard_login()
    test.driver.implicitly_wait(5)

@when('we click the login button')
def step_impl(context):
    test.login_page.click_login_button()
    test.driver.implicitly_wait(5)

@then('we are redirected to Sauce Demo main page')
def step_impl(context):
    assert test.driver.current_url == "https://www.saucedemo.com/inventory.html"

@then('we verify the app logo exists')
def step_impl(context):
    logo_present = test.home_page.confirm_logo_presence()
    assert logo_present is True

@when('we fill account info for blocked user')
def step_impl(context):
    test.login_page.fill_failed_login()
    test.driver.implicitly_wait(5)

@then('we verify the error message reads "Sorry, this user has been banned."')
def step_impl(context):
    error_message = test.login_page.read_error()
    assert error_message == "Sorry, this user has been banned."
