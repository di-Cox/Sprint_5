from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from data import MyPersonalData


# Тест проверяет выхода пользователя из личного кабинета
def test_logout_from_personal_account(driver):
    # Заходим на главную страницу
    driver.get(main_site)

    # Нажимаем кнопку "Личный кабинет" на главной странице
    driver.find_element(*Locators.button_personal_account).click()

    # Заполняем поле "Email" для входа
    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

    # Заполняем поле "Пароль" для входа
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

    # Нажимаем кнопку "Войти"
    driver.find_element(*Locators.button_login).click()

    # Снова переходим в личный кабинет, чтобы дождаться полной загрузки страницы
    driver.find_element(*Locators.button_personal_account).click()

    # Ожидаем появления кнопки "Профиль" для подтверждения загрузки личного кабинета
    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located(Locators.button_inscription_profile)
    )

    # Нажимаем кнопку "Выйти"
    driver.find_element(*Locators.button_inscription_exit).click()

    # Ожидаем появления кнопки "Войти" после выхода из аккаунта
    login_button = WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located(Locators.button_login)
    )

    # Проверяем, что после выхода действительно отображается кнопка "Войти"
    assert login_button.text == "Войти"

