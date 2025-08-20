import pytest
from locators import Locators
from data import MyPersonalData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *


class TestPersonalAccount:

    # Тест перехода в личный кабинет
    def test_go_to_personal_account(self, driver):
        # Заходим на главную страницу
        driver.get(main_site)

        # Нажимаем кнопку "Личный кабинет"
        driver.find_element(*Locators.button_personal_account).click()

        # Вводим Email и Пароль
        driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
        driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login).click()

        # После входа снова переходим в личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        # Ждём загрузки кнопки "Профиль"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.button_inscription_profile)
        )

        # Проверяем, что кнопка "Профиль" отображается
        assert driver.find_element(*Locators.button_inscription_profile).is_displayed(), \
            "Кнопка 'Профиль' не отображается — личный кабинет не открылся"

    # Тест перехода из личного кабинета в конструктор через кнопку "Конструктор"
    def test_return_to_constructor_via_constructor_button(self, driver):
        # Заходим на главную страницу
        driver.get(main_site)

        # Нажимаем кнопку "Личный кабинет"
        driver.find_element(*Locators.button_personal_account).click()

        # Вводим Email и Пароль
        driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
        driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login).click()

        # После входа снова переходим в личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        # Ждём загрузки кнопки "Профиль"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.button_inscription_profile)
        )

        # Нажимаем кнопку "Конструктор"
        driver.find_element(*Locators.button_constructor).click()

        # Ждём видимости раздела "Булки"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_bread)
        )

        # Проверяем, что раздел "Булки" отображается
        assert driver.find_element(*Locators.section_bread).is_displayed(), \
            "Раздел 'Булки' не открылся после перехода через кнопку 'Конструктор'"

    # Тест перехода из личного кабинета в конструктор через логотип Stellar Burgers
    def test_return_to_constructor_via_logo(self, driver):
        # Заходим на главную страницу
        driver.get(main_site)

        # Нажимаем кнопку "Личный кабинет"
        driver.find_element(*Locators.button_personal_account).click()

        # Вводим Email и Пароль
        driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
        driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)

        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.button_login).click()

        # После входа снова переходим в личный кабинет
        driver.find_element(*Locators.button_personal_account).click()

        # Ждём загрузки кнопки "Профиль"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.button_inscription_profile)
        )

        # Нажимаем на логотип Stellar Burgers
        driver.find_element(*Locators.logo).click()

        # Ждём видимости раздела "Булки"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_bread)
        )

        # Проверяем, что раздел "Булки" отображается
        assert driver.find_element(*Locators.section_bread).is_displayed(), \
            "Раздел 'Булки' не открылся после перехода через логотип Stellar Burgers"