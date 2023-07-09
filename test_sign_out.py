import json
from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestSignOut:
    def test_sign_out_true(self):
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
       # fake = Faker()
        # Открыть сайт
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Найти кнопку Личный кабинет и кликнуть
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Вход')]")))
        with open("fake_data.json", mode="r", encoding="utf-8") as f:
            fdl = json.load(f)
        fdl_email = fdl['email'] # Заполняем данные из файла созданного при регистрации

        # Найти поле "Логин" и заполнить его
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys(fdl_email)

        # Найти поле "Пароль" и заполнить его
        driver.find_element(By.NAME, "Пароль").clear()
        driver.find_element(By.NAME, "Пароль").send_keys("123456")

        # Найти кнопку "Войти" и кликнуть по ней
        driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")))
        # опять переходим в личный кабинет
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[contains(text(), 'Профиль')]")))
        driver.find_element(By.XPATH, ".//button[contains(text(), 'Выход')]").click() # Нажимаем на "выход"
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Вход')]")))
        assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]")
        driver.quit()


