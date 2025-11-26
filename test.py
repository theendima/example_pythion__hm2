from selene import browser, be,have


browser.open('https://animevost.org/')
browser.element('#login_name').set_value('endima')
browser.element('#login_password').set_value('test').press_enter()
browser.element('a[href="/dlya-pravoobladateley.html"]').click()














#browser.element('#href="/dlya-pravoobladateley.html').should(be.blank).type('Правообладателям')
#browser.element('#login_submit').click()
#browser.element('#submit').click()

browser.quit()



#value="Пароль"
#browser.element('[name="login_name"]').should(be.blank).type('endima')

