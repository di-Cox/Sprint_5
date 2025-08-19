import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *
from data import SectionTitles


class TestConstructorSections:

    # Тест проверяет переход в раздел "Булки"
    def test_go_to_buns_section(self, driver):
        # Открываем главную страницу "Stellar Burgers"
        driver.get(main_site)

        # Сначала переходим в раздел "Соусы"
        driver.find_element(*Locators.inscription_sause).click()
        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(Locators.section_sause)
        )

        # Затем переходим в раздел "Булки"
        driver.find_element(*Locators.inscription_bread).click()

        # Ожидаем появления списка булок
        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(Locators.section_bread)
        )

        # Получаем текст заголовка раздела "Булки"
        section_text = driver.find_element(*Locators.inscription_bread).text

        # Проверяем, что заголовок раздела соответствует "Булки"
        assert section_text == SectionTitles.BUNS

        # Проверяем, что список булок отображается
        assert driver.find_element(*Locators.section_bread).is_displayed()

    # Тест проверяет переход в раздел "Соусы"
    def test_go_to_sauces_section(self, driver):
        # Открываем главную страницу "Stellar Burgers"
        driver.get(main_site)

        # Кликаем по кнопке "Соусы"
        driver.find_element(*Locators.inscription_sause).click()

        # Ожидаем появления списка соусов
        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(Locators.section_sause)
        )

        # Получаем текст заголовка раздела "Соусы"
        section_text = driver.find_element(*Locators.inscription_sause).text

        # Проверяем, что заголовок раздела соответствует "Соусы"
        assert section_text == SectionTitles.SAUCES

        # Проверяем, что список соусов отображается
        assert driver.find_element(*Locators.section_sause).is_displayed()

    # Тест проверяет переход в раздел "Начинки"
    def test_go_to_fillings_section(self, driver):
        # Открываем главную страницу "Stellar Burgers"
        driver.get(main_site)

        # Кликаем по кнопке "Начинки"
        driver.find_element(*Locators.inscription_filling).click()

        # Ожидаем появления списка начинок
        WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(Locators.section_filling)
        )

        # Получаем текст заголовка раздела "Начинки"
        section_text = driver.find_element(*Locators.inscription_filling).text

        # Проверяем, что заголовок раздела соответствует "Начинки"
        assert section_text == SectionTitles.FILLINGS

        # Проверяем, что список начинок отображается
        assert driver.find_element(*Locators.section_filling).is_displayed()


