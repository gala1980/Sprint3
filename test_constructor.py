
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ClickLocators:
    sauce = [By.XPATH, ".//span[contains(text(), 'Соусы')]"]
    bread = [By.XPATH, ".//span[contains(text(), 'Булки')]"]
    filling = [By.XPATH, ".//span[contains(text(), 'Начинки')]"]

    def __init__(self, driver):
        self.driver = driver


    # метод кликает по кнопке «Соусы»
    def click_sauce_button(self):
        self.driver.find_element(*self.sauce).click()
        return self.driver.find_element(*self.sauce).text


    # метод кликает по кнопке «Булки»
    def click_bread_button(self):
        self.driver.find_element(*self.bread).click()
        return self.driver.find_element(*self.bread).text


    # метод кликает по кнопке «Начинки»
    def click_filling_button(self):
        self.driver.find_element(*self.filling).click()
        return self.driver.find_element(*self.filling).text


class TextLocators:
    h2_sauce = [By.XPATH, ".//h2[contains(text(), 'Соусы')]"]
    h2_bread = [By.XPATH, ".//h2[contains(text(), 'Булки')]"]
    h2_filling = [By.XPATH, ".//h2[contains(text(), 'Начинки')]"]

    def __init__(self, driver):
        self.driver = driver


    def get_description_sauce(self):
        return self.driver.find_element(*self.h2_sauce).text

    def get_description_bread(self):
        return self.driver.find_element(*self.h2_bread).text

    def get_description_filling(self):
        return self.driver.find_element(*self.h2_filling).text

class TestConstructor:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()


    def test_check_to_sauce(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        locators_click = ClickLocators(self.driver)
        text_locator_click = locators_click.click_sauce_button()
        text_locators = TextLocators(self.driver)
        text_locator_h2 = text_locators.get_description_sauce()
        assert text_locator_click == text_locator_h2  # Проверяем, что Соусы из таблицы совпадают с названием Соусов из заголовка


    def test_check_to_bread(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        locators_click = ClickLocators(self.driver)
        text_locator_click = locators_click.click_sauce_button()
        text_locator_click = locators_click.click_bread_button()
        text_locators = TextLocators(self.driver)
        text_locator_h2 = text_locators.get_description_bread()
        assert text_locator_click == text_locator_h2  # Проверяем, что Соусы из таблицы совпадают с названием Соусов из заголовка


    def test_check_to_filling(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        locators_click = ClickLocators(self.driver)
        text_locator_click = locators_click.click_filling_button()
        text_locators = TextLocators(self.driver)
        text_locator_h2 = text_locators.get_description_filling()
        assert text_locator_click == text_locator_h2  # Проверяем, что Соусы из таблицы совпадают с названием Соусов из заголовка


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
