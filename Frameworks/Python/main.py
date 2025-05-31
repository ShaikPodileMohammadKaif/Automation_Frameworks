from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
class TestYatra:
    def test_yatra(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://www.yatra.com")
        print("Yatra website opened successfully")
        driver.maximize_window()
        time.sleep(5)
        login_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div[2]/div[3]/p/span/span').click()
        driver.find_element(By.XPATH,'//*[@id="simple-popover"]/div[3]/div/div/p[1]').click()
        print(driver.current_url)
        print(driver.title)
        time.sleep(5)
        print("Welcome to Yatra")
        driver.find_element(By.NAME,"login-input").send_keys("kaifpodille95@gmail.com")
        driver.find_element(By.ID,"login-continue-btn").click()
        time.sleep(5)
        driver.find_element(By.ID,"signup-mobile-number").send_keys("7981486928")
        driver.find_element(By.ID,"signup-password").send_keys("Kaif@123")

        Select(driver.find_element(By.ID,"signup-user-designation")).select_by_index(2)
        driver.find_element(By.ID,"signup-user-first-name").send_keys("Mohammad")
        driver.find_element(By.ID, "signup-user-last-name").send_keys("Kaif")
        driver.find_element(By.XPATH, '//*[@id="signup-form-continue-btn"]').click()
        time.sleep(5)
        print("Login successful")
        driver.close()
a = TestYatra()
a.test_yatra()