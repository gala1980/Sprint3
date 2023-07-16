import json
from selenium import webdriver
from faker import Faker
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def redirect_to_LKK(driver, flag_tpa=False): # Создаем функцию входа в личный кабинет, чтоб потом использовать в тесте (чтоб два раза не прописывать одинаковые шаги)
    fake = Faker()
    # Открыть сайт
    driver.get("https://stellarburgers.nomoreparties.site/")
    # Найти кнопку Личный кабинет и кликнуть
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    WebDriverWait(driver, 20).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Вход')]")))
    with open("fake_data.json", mode="r", encoding="utf-8") as f:
        fdl = json.load(f)
    fdl_email = fdl['email']  # Заполняем данные из файла созданного при регистрации

    # Найти поле "Логин" и заполнить его
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(fdl_email)

    # Найти поле "Пароль" и заполнить его
    driver.find_element(By.NAME, "Пароль").clear()
    driver.find_element(By.NAME, "Пароль").send_keys("123456")

    # Найти кнопку "Войти" и кликнуть по ней
    driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]").click()
    WebDriverWait(driver, 20).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    WebDriverWait(driver, 20).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//a[contains(text(), 'Профиль')]")))
    login_email = driver.find_element(By.XPATH, ".//li[2]/div/div/input").get_attribute('value') # записываем в переменную значение атрибута чтоб потом сравнить с fdl
    if flag_tpa: # По умолчанию флаг False, ничего не передаем
        return fdl_email, login_email


class TestRedirectAccount:
    def test_to_personal_accaunt_true(self): # Проверка перехода по клику на «Личный кабинет».
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)

        fdl_email, login_email = redirect_to_LKK(driver, True) # меняем флаг на True, возвращаем данные из поля "Логин" и из файла fake_data.json
        assert login_email == fdl_email # Проверяем, что переменная из поля "Логин" равна значению из файла с данными по пользователю (fake_data.json)
        driver.quit()

    def test_redirect_from_LKK_to_constructor_true(self): # Переход из личного кабинета в конструктор
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
        redirect_to_LKK(driver) # вызываем функцию которая открывает личный кабинет
        driver.find_element(By.XPATH, ".//a/p[contains(text(), 'Конструктор')]").click()
        assert driver.find_element(By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")
        driver.quit()

