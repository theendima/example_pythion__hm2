from selene import browser, be, have, by



browser.open('https://makler.md/')
browser.element('#logInDiv').click()
browser.element('[name="login"]').set_value('test@mail.ru')
browser.element('[name="password"]').should(be.visible).set_value('test').press_enter()
browser.element('.header_menuLink').click()
browser.element('#pageTopId').should(have.text('Подписки'))
browser.quit()





