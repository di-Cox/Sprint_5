import pytest
from locators import Locators
from data import MyPersonalData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *


class TestLogin:

    # Тест проверки входа через кнопку "Войти в аккаунт" на главной странице Stellar Burgers
    def test_login_via_login_to_account_button(self, driver):
        # Заходим на главную страницу
        driver.get(main_site)

        # Нажимаем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.button_login_to_account).click()

        # Заполняем поле Email
        driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

        # Заполняем поле Пароль
        driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login).click()

        # Ожидаем появления кнопки "Оформить заказ"
        place_order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.button_place_an_order)
        )

        # Проверяем, что кнопка "Оформить заказ" действительно отображается на странице
        assert place_order_button.text == "Оформить заказ"

    # Тест проверки входа через кнопку "Личный кабинет" на главной странице Stellar Burgers
    def test_login_via_personal_account_button(self, driver):
        # Заходим на главную страницу
        driver.get(main_site)

        # Нажимаем кнопку "Личный кабинет"
        driver.find_element(*Locators.button_personal_account).click()

        # Заполняем поле Email
        driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

        # Заполняем поле Пароль
        driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login).click()

        # Ожидаем появления кнопки "Оформить заказ"
        place_order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.button_place_an_order)
        )

        # Проверяем, что кнопка "Оформить заказ" действительно отображается на странице
        assert place_order_button.text == "Оформить заказ"

    # Тест проверки входа через кнопку "Войти" в форме регистрации /register
    def test_login_via_registration_page(self, driver):
        # Заходим на страницу регистрации
        driver.get(register_site)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_inscription_login).click()

        # Заполняем поле Email
        driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

        # Заполняем поле Пароль
        driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login).click()

        # Ожидаем появления кнопки "Оформить заказ"
        place_order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.button_place_an_order)
        )

        # Проверяем, что кнопка "Оформить заказ" действительно отображается на странице
        assert place_order_button.text == "Оформить заказ"

    # Тест проверки входа через кнопку "Войти" в форме восстановления пароля
    def test_login_via_recover_password(self, driver):
        # Заходим на страницу входа
        driver.get(login_site)

        # Нажимаем кнопку "Восстановить пароль"
        driver.find_element(*Locators.button_inscription_recover_password).click()

        # Ждем загрузку кнопки "Войти"
        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(Locators.button_inscription_login)
        )

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_inscription_login).click()

        # Заполняем поле Email
        driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)

        # Заполняем поле Пароль
        driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login).click()

        # Ожидаем появления кнопки "Оформить заказ"
        place_order_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.button_place_an_order)
        )

        # Проверяем, что кнопка "Оформить заказ" действительно отображается на странице
        assert place_order_button.text == "Оформить заказ"