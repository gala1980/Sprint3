import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRedirectAccount:
    def test_redirect_to_sauce(self):
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Соусы')]").click()
        list_element = driver.find_element(By.XPATH, ".//span[contains(text(), 'Соусы')]").text
        heading_element = driver.find_element(By.XPATH, ".//h2[contains(text(), 'Соусы')]").text
        assert list_element == heading_element  # Проверяем, что Соусы из таблицы совпадают с названием Соусов из заголовка
        driver.quit()


    def test_redirect_to_bread(self):
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Соусы')]").click()
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Булки')]").click()
        list_element = driver.find_element(By.XPATH, ".//span[contains(text(), 'Булки')]").text
        heading_element = driver.find_element(By.XPATH, ".//h2[contains(text(), 'Булки')]").text
        assert list_element == heading_element  # Проверяем, что булки из таблицы совпадают с названием Булок из заголовка
        driver.quit()



    def test_redirect_to_filling(self):
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//span[contains(text(), 'Начинки')]").click()
        list_element = driver.find_element(By.XPATH, ".//span[contains(text(), 'Начинки')]").text
        heading_element = driver.find_element(By.XPATH, ".//h2[contains(text(), 'Начинки')]").text
        assert list_element == heading_element  # Проверяем, что Начинки из таблицы совпадают с названием Начинки из заголовка
