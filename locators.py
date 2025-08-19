from selenium.webdriver.common.by import By

class Locators:

    # Кнопка "Войти в аккаунт" на главной странице
    button_login_to_account = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')

    # Поле ввода "Email" в форме "Вход"
    input_field_email = (By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input')

    # Поле ввода "Пароль" в форме "Вход"
    input_field_password = (By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input')

    # Кнопка "Войти" в форме "Вход"
    button_login = (By.XPATH, '//button[contains(text(),"Войти")]')

    # Основное "Лого" главной страницы
    logo = (By.XPATH, '//header/nav/div')

    # Надпись "Булки"
    inscription_bread = (By.XPATH, '//span[contains(text(),"Булки")]')

    # Надпись "Соусы"
    inscription_sause = (By.XPATH, '//span[contains(text(),"Соусы")]')

    # Надпись "Начинки"
    inscription_filling = (By.XPATH, '//span[contains(text(),"Начинки")]')

    # Кнопка "Конструктор"
    button_constructor = (By.XPATH, '//a[@href="/"]')

    # Кнопка "Лента Заказов"
    button_order_feed = (By.XPATH, '//a[@href="/feed"]')

    # Кнопка "Оформить заказ"
    button_place_an_order = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')

    # Кнопка "Личный Кабинет"
    button_personal_account = (By.XPATH, '//a[@href="/account"]')

    # Кнопка-надпись "Выход" в "Личном Кабинете"
    button_inscription_exit = (By.XPATH, '//button[contains(text(),"Выход")]')

    # Кнопка-надпись "Профиль" в "Личном Кабинете"
    button_inscription_profile = (By.XPATH, '//a[@href="/account/profile"]')

    # Кнопка-надпись "История заказов" в "Личном Кабинете"
    button_inscription_order_history = (By.XPATH, '//a[@href="/account/order-history"]')

    # Кнопка-надпись "Отмена" в "Личном Кабинете"
    button_inscription_cancel = (By.XPATH, '//button[contains(text(),"Отмена")]')

    # Кнопка "Сохранить" в "Личном Кабинете"
    button_save = (By.XPATH, '//button[contains(text(),"Сохранить")]')

    # Кнопка-надпись "Зарегистрироваться"
    button_inscription_register = (By.XPATH, '//a[@href="/register"]')

    # Поле ввода "Имя" в форме "Регистрация"
    input_name = (By.XPATH, '//div[label[contains(text(), "Имя")]]//input')

    # Поле ввода "Email" в форме "Регистрация"
    input_email = (By.XPATH, '//div[label[contains(text(), "Email")]]//input')

    # Поле ввода "Пароля" в форме "Регистрация"
    input_password = (By.XPATH, '//div[label[contains(text(), "Пароль")]]//input')

    # Кнопка "Зарегистрироваться" в форме "Регистрация"
    button_register = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')

    # Кнопка-надпись "Войти" в форме "Регистрация"
    button_inscription_login = (By.XPATH, '//a[@href="/login"]')

    # Кнопка-надпись "Восстановить пароль"
    button_inscription_recover_password = (By.XPATH, '//a[@href="/forgot-password"]')

    # Поле ввода "Email" в форме "Восстановление пароля"
    input_restore_email = (By.XPATH, '//div[label[contains(text(), "Email")]]//input')

    # Кнопка "Восстановить" в форме "Восстановление пароля"
    button_restore = (By.XPATH, '//button[contains(text(), "Восстановить")]')

    # Поле ввода "Пароль" в форме "Восстановление пароля"
    input_restore_password = (By.XPATH, '//div[label[contains(text(), "Пароль")]]//input')

    # Поле ввода "Введите код из письма" в форме "Восстановление пароля"
    input_enter_the_code = (By.XPATH, '//div[label[contains(text(), "Введите код из письма")]]//input')

    # Отображение надписи "Некорректный пароль" в формах заполнения пароля
    message_incorrect_password = (By.XPATH, '//div[contains(@class, "input_status_error")]')

    # Текстовая надпись "Булки"
    section_bread = (By.XPATH, '//h2[text()="Булки"]')

    # Текстовая надпись "Соусы"
    section_sause = (By.XPATH, '//h2[text()="Соусы"]')

    # Текстовая надпись "Начинки"
    section_filling = (By.XPATH, '//h2[text()="Начинки"]')
