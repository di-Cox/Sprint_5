

import pytest
from selenium import webdriver
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import login_site
from geniration_ep import EmailPasswordGenerator
from data import MyPersonalData


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

    # "Регистрация" на странице /login

@pytest.fixture
def start_from_successful_registration(driver):
    login_page = login_site
    driver.get(login_page)          # Заходим на страницу формы "Вход"

    # Заполняем поля "Email" и "Пароль" затем нажимаем кнопку "Войти"

    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)
    driver.find_element(*Locators.button_login).click()

    return driver

    # "Восстановить пароль"

@pytest.fixture
def start_from_recover_password(driver):
    login_page = login_site
    driver.get(login_page)          # Заходим на страницу формы "Вход"

    # Переходим по кнопки-надписи "Восстановить пароль"
    driver.find_element(*Locators.button_inscription_recover_password).click()

    # Ожидаем загрузку кнопки "Войти"
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.button_inscription_login))

    # Нажимаем на кнопку-надпись "Войти"
    driver.find_element(*Locators.button_inscription_login).click()

    # Заполняем поля "Email" и "Пароль" затем нажимаем кнопку "Войти"

    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)
    driver.find_element(*Locators.button_login).click()

    return driver

    # "Зарегистрироваться"

@pytest.fixture
def start_from_register_button(driver):
    login_page = login_site
    driver.get(login_page)          # Заходим на страницу формы "Вход"

    # Нажимаем на кнопку-надпись "Зарегистрироваться"
    driver.find_element(*Locators.button_inscription_register).click()

    # Ожидаем загрузку кнопки "Войти"
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.button_inscription_login))

    # Заполняем поля "Email" и "Пароль" затем нажимаем кнопку "Войти"

    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)
    driver.find_element(*Locators.button_login).click()

    return driver

    # "Личный Кабинет"

@pytest.fixture
def start_from_personal_account_button(driver):
    login_page = main_site
    driver.get(login_page)          # Заходим на главную страницу "Stellarburgers"

    # Нажимаем кнопку "Личный Кабинет"
    driver.find_element(*Locators.button_personal_account).click()

    # Заполняем поля "Email" и "Пароль" затем нажимаем кнопку "Войти"

    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)
    driver.find_element(*Locators.button_login).click()

    return driver


    # "Войти в аккаунт"
@pytest.fixture
def start_from_login_to_account_button(driver):
    login_page = main_site
    driver.get(login_page)          # Заходим на главную страницу "Stellarburgers"

    # Нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*Locators.button_login_to_account).click()

    # Заполняем поля "Email" и "Пароль" затем нажимаем кнопку "Войти"

    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)
    driver.find_element(*Locators.button_login).click()

    return driver


    # Переход по кнопки-надписи "Войти" напрямую через /register
@pytest.fixture
def start_from_registration_via_login(driver):
    login_page = register_site
    driver.get(login_page)          # Заходим на страницу с "Регистрацией"

    # Нажимаем на кнопу-надпись "Войти"
    driver.find_element(*Locators.button_inscription_login).click()

    # Заполняем поля "Email" и "Пароль" затем нажимаем кнопку "Войти"

    driver.find_element(*Locators.input_field_email).send_keys(MyPersonalData.email)
    driver.find_element(*Locators.input_field_password).send_keys(MyPersonalData.password)
    driver.find_element(*Locators.button_login).click()

    return driver


    # Заходим на главную страницу "Stellarburgers"
@pytest.fixture
def open_the_main_page(driver):
    login_page = main_site
    driver.get(login_page)          # Заходим на главную страницу "Stellarburgers"

    # Заходим на страницу формы "Вход"
@pytest.fixture
def open_the_login_page(driver):
    login_page = login_site
    driver.get(login_page)          # Заходим на страницу формы "Вход"

    # Заходим на страницу с "Регистрацией"
@pytest.fixture
def open_the_registration_page(driver):
    login_page = register_site
    driver.get(login_page)          # Заходим на страницу с "Регистрацией"
    return driver


    # Регистрация нового аккаунта
@pytest.fixture
def registering_new_account(driver):
    login_page = login_site
    driver.get(login_page)          # Заходим на страницу формы "Вход"

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(*Locators.button_inscription_register).click()

    # Генерируем "Email" и "Пароль"
    generator = EmailPasswordGenerator()
    email, password = generator.generate()

    # Ищем и заполняем поле "Имя"
    driver.find_element(*Locators.input_name).send_keys(MyPersonalData.name)

    # Ищем и заполняем поле "Email"
    driver.find_element(*Locators.input_email).send_keys(email)

    # Ищем и заполняем поле "Пароль"
    driver.find_element(*Locators.input_password).send_keys(password)

    # Нажимаем на кнопку "Зарегистрироваться"
    driver.find_element(*Locators.button_register).click()

    # Ждем отображения кнопки "Войти"
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.button_login))

    return driver, email, password












