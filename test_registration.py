import json

from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_redirect_to_login_accaunt_true(self):
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
        # Зайти на сайт
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Найти кнопку Личный кабинет и кликнуть
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        # Проверить, что перешли на страницу Входа
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_redirect_to_create_new_accaunt_true(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        #Найти кнопку Зарегистрироваться и кликнуть
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        WebDriverWait(driver, 20)
        # Проверить, что перешли на страницу Регистрации
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

    def test_fill_registration_data_true(self):
        fake = Faker()
        fakeData = {"name": fake.name(),
                    "email": fake.ascii_free_email()} # Создаем словарь для записи рандомных данных
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Найти поле "Имя" и заполнить его
        driver.find_element(By.NAME, "name").send_keys(fakeData["name"])

        # Найти поле "Email" и заполнить его
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").clear()
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(fakeData["email"])

        #Найти поле "Пароль" и заполнить его
        driver.find_element(By.NAME, "Пароль").clear()
        driver.find_element(By.NAME, "Пароль").send_keys("123456")

        # Найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]").click()
        with open("fake_data.json", mode="w+", encoding="utf-8") as f:
            json.dump(fakeData, f, indent=4, ensure_ascii=False) # Запись в json данных аккаунта, чтобы потом их выдернуть для проверки
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Вход')]")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()


