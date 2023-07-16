from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import redirect_to_LKK

class TestSignOut:
    def test_sign_out_true(self):
        driver = webdriver.Chrome()
        redirect_to_LKK(driver)
        #driver.get("https://stellarburgers.nomoreparties.site/")
        # опять переходим в личный кабинет
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[contains(text(), 'Профиль')]")))
        driver.find_element(By.XPATH, ".//button[contains(text(), 'Выход')]").click() # Нажимаем на "выход"
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(), 'Вход')]")))
        assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Войти')]")
        driver.quit()


