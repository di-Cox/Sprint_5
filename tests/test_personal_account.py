import pytest
from locators import Locators
from data import MyPersonalData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *

# Тест перехода в личный кабинет
def test_go_to_personal_account(driver):
    # Заходим на главную страницу
    driver.get(main_site)

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*Locators.button_personal_account).click()

    # Вводим Email в поле "Email"
    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

    # Вводим Пароль в поле "Пароль"
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

    # Нажимаем кнопку "Войти"
    driver.find_element(*Locators.button_login).click()

    # После входа повторно переходим в личный кабинет
    driver.find_element(*Locators.button_personal_account).click()

    # Ожидаем загрузку личного кабинета по видимости кнопки "Профиль"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_inscription_profile))


# Тест перехода из личного кабинета в конструктор через кнопку "Конструктор"
def test_return_to_constructor_via_constructor_button(driver):
    # Заходим на главную страницу
    driver.get(main_site)

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*Locators.button_personal_account).click()

    # Вводим Email в поле "Email"
    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

    # Вводим Пароль в поле "Пароль"
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

    # Нажимаем кнопку "Войти"
    driver.find_element(*Locators.button_login).click()

    # После входа повторно переходим в личный кабинет
    driver.find_element(*Locators.button_personal_account).click()

    # Ожидаем загрузку личного кабинета по видимости кнопки "Профиль"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_inscription_profile))

    # Нажимаем кнопку "Конструктор"
    driver.find_element(*Locators.button_constructor).click()

    # Ожидаем видимость раздела "Булки" для подтверждения перехода
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

# Тест перехода из личного кабинета в конструктор через логотип Stellar Burgers
def test_return_to_constructor_via_logo(driver):
    # Заходим на главную страницу
    driver.get(main_site)

    # Нажимаем кнопку "Личный кабинет"
    driver.find_element(*Locators.button_personal_account).click()

    # Вводим Email в поле "Email"
    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

    # Вводим Пароль в поле "Пароль"
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

    # Нажимаем кнопку "Войти"
    driver.find_element(*Locators.button_login).click()

    # После входа повторно переходим в личный кабинет
    driver.find_element(*Locators.button_personal_account).click()

    # Ожидаем загрузку личного кабинета по видимости кнопки "Профиль"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_inscription_profile))

    # Нажимаем на логотип Stellar Burgers
    driver.find_element(*Locators.logo).click()

    # Ожидаем видимость раздела "Булки" для подтверждения перехода в конструктор
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))