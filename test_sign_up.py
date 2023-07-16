from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import sign_up


class TestSignUp:

    def test_sign_from_main_page_true(self):
        driver = webdriver.Chrome()
        sign_up(driver)
        # Найти кнопку "Войти" и кликнуть по ней
        driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")))
        order = driver.find_element(By.XPATH, ".//button[starts-with(@class, 'button')]")
        assert order.text == "Оформить заказ"
        driver.quit()

    def test_sign_from_password_page_true(self):
        driver = webdriver.Chrome()
        fake = Faker()
        # Открыть сайт
        driver.get("https://stellarburgers.nomoreparties.site/")
        # Найти кнопку "Войти в аккаунт" и кликнуть
        driver.find_element(By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Вход')]")))
        driver.find_element(By.XPATH, ".//a[contains(text(),'Восстановить пароль')]").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Восстановление пароля')]")))
        driver.find_element(By.XPATH, ".//a[contains(text(),'Войти')]").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Вход')]")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()