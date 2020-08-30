from behave import given, when, then
from selenium.webdriver.support.ui import Select


@given('As a client I want to log in as "{name}" properly and balance is 0')
def step_impl(context, name):
    context.helper.open("http://www.way2automation.com/angularjs-protractor/banking/#/login")
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[1]/button").click()
    drop = context.helper.find_by_xpath('//*[@id="userSelect"]')
    context.drop_select = Select(drop)
    context.drop_select.select_by_visible_text(name)
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/form/button").click()
    if int(context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/strong[2]").text) != 0:
        context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/button[1]").click()
        context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/button[2]").click()
        context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/button[1]").click()


@when('I make deposit: "{deposit}" for user: "{name}"')
def step_impl(context, deposit, name):
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/button[2]").click()
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[4]/div/form/div/input").send_keys(deposit)
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[4]/div/form/button").click()
    try:
        information = "Deposit Successful"
        information_website = context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[4]/div/span").text
        assert information_website == information
    except AssertionError:
        context.helper.screenshot(name)
        print("Test Failure")
        raise AssertionError


@when('Balance is changed : "{deposit}" for user: "{name}"')
def step(context, deposit, name):
    try:
        deposit_website = int(context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/strong[2]").text)
        assert deposit_website == int(deposit)
    except AssertionError:
        context.helper.screenshot(name)
        print("Test Failure")
        raise AssertionError


@when('I make the withdrawl: "{withdrawl}"')
def step(context, withdrawl):
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/button[3]").click()
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[4]/div/form/div/input").send_keys(withdrawl)
    context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[4]/div/form/button").click()


@then('Balance is changed for "{end_balance}" and if test fail screenshot is captured as file: "{name}".png')
def step(context, end_balance, name):
    try:
        website_value = int(context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/strong[2]").text)
        information = "Transaction successful"
        information_website = context.helper.find_by_xpath("/html/body/div[3]/div/div[2]/div/div[4]/div/span").text
        assert website_value == int(end_balance)
        assert information == information_website
    except AssertionError:
        context.helper.screenshot(name)
        print("Test Failure")
        raise AssertionError
