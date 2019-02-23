from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import sys


@pytest.fixture(scope="function")
def get_driver(request):
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.set_window_size(1200, 800)
    driver.get("https://opensource-demo.orangehrmlive.com")
    yield
    time.sleep(5)
    driver.close()
    driver.quit()
    print("Test Completed")
    print(sys.path)
