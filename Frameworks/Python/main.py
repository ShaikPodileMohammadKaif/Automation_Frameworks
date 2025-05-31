from selenium import webdriver
import time
class TestYatra:
    def test_yatra(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com")
        print("Yatra website opened successfully")
        driver.maximize_window()
        time.sleep(10)
        driver.close()
a = TestYatra()
a.test_yatra()