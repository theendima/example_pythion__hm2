import pytest
#from past.translation import autotranslate
from selene import browser, be, have
from selenium import webdriver



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://makler.md/'
    browser.config.browser_type = 'chrome'
    #browser.config.timeout = 10
    browser.config.driver_name = 'chromedriver'

 #driver_options = webdriver.ChromeOptions()   - для плохой сети
 #driver_options.add_argument('eager')



def test_login():
    browser.open('')
    browser.element('#logInDiv').click()
    browser.element('[name="login"]').set_value('test')
    browser.element('[name="password"]').should(be.visible).set_value('test').press_enter()
    browser.quit()


def test_valid_helper():
    browser.open('')
    browser.element('#logInDiv').click()
    browser.element('[name="login"]').set_value('test')
    browser.element('[name="password"]').should(be.visible).set_value('test').press_enter()
    browser.element('.header_menuLink').click()
    browser.element('#pageTopId').should(have.text('Подписки'))
    browser.quit()


def test_wrong():
    browser.open('')
    browser.element('#logInDiv').click()
    browser.element('[name="login"]').set_value('test')
    browser.element('[name="password"]').should(be.visible).set_value('1').press_enter()
    browser.element('[class="valid validMail"]').should(have.text('Вы ввели неверный логин или пароль'))
    browser.quit()



