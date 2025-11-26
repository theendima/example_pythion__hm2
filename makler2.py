from selene import browser, be, have, by


def test_login():
    browser.open('https://makler.md/')
    browser.element('#logInDiv').click()
    browser.element('[name="login"]').set_value('test@mail.ru')
    browser.element('[name="password"]').should(be.visible).set_value('CG5yiZZRkPzPXp7').press_enter()
    browser.quit()


def test_valid_helper():
    browser.open('https://makler.md/')
    browser.element('#logInDiv').click()
    browser.element('[name="login"]').set_value('test@mail.ru')
    browser.element('[name="password"]').should(be.visible).set_value('CG5yiZZRkPzPXp7').press_enter()
    browser.element('.header_menuLink').click()
    browser.element('#pageTopId').should(have.text('Подписки'))
    browser.quit()


def test_wrong():
    browser.open('https://makler.md/')
    browser.element('#logInDiv').click()
    browser.element('[name="login"]').set_value('test@mail.ru')
    browser.element('[name="password"]').should(be.visible).set_value('1').press_enter()
    browser.element('[class="valid validMail"]').should(have.text('Вы ввели неверный логин или пароль'))
    browser.quit()



