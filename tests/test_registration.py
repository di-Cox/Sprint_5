from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from geniration_ep import EmailPasswordGenerator
from data import MyPersonalData
from locators import Locators
from curl import *

# Тест проверяет успешную регистрацию нового пользователя
def test_successful_registration(driver):
    # Заходим на страницу входа
    driver.get(login_site)

    # Нажимаем на кнопку "Зарегистрироваться"
    driver.find_element(*Locators.button_inscription_register).click()

    # Генерируем email и пароль с помощью geniration_ep.py
    generator = EmailPasswordGenerator()
    email, password = generator.generate()

    # Заполняем поле "Имя" (используем имя из data.py)
    driver.find_element(*Locators.input_name).send_keys(MyPersonalData.name)

    # Заполняем поле "Email" (сгенерированный email)
    driver.find_element(*Locators.input_email).send_keys(email)

    # Заполняем поле "Пароль" (сгенерированный пароль)
    driver.find_element(*Locators.input_password).send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(*Locators.button_register).click()

    # Ждём появления кнопки "Войти"
    WebDriverWait(driver, 8).until(
        EC.visibility_of_element_located(Locators.button_login))

    # Проверяем, что после успешной регистрации действительно появилась кнопка "Войти"
    assert driver.find_element(*Locators.button_login).is_displayed(), \
        "Кнопка 'Войти' не отобразилась после регистрации"


# Тест на проверку вывода ошибки при некорректном пароле
def test_incorrect_password_error(driver):
    # Заходим на страницу входа
    driver.get(login_site)

    # Заполняем поле "Email"
    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

    # Заполняем поле "Пароль" некорректным значением
    driver.find_element(*Locators.input_field_password).send_keys('12345')

    # Нажимаем кнопку "Войти"
    driver.find_element(*Locators.button_login).click()

    # Ожидаем отображение сообщения об ошибке некорректного пароля
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.message_incorrect_password))

    # Проверка: сообщение об ошибке действительно отображается
    assert driver.find_element(*Locators.message_incorrect_password).is_displayed(), \
        "Сообщение об ошибке некорректного пароля не появилось"