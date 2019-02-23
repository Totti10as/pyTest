from selenium import webdriver
from Pages.loginpage import LoginPage
from Pages.homepage import HomePage
from allure_commons.types import AttachmentType
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import allure
import sys


@allure.feature('Login')
@allure.story('Enter into user account')
@allure.severity('blocker')


class TestLoign():
    @pytest.fixture()
    def setup_method(self):
        global driver
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.set_window_size(1200, 800)
        yield
        time.sleep(5)
        driver.close()
        driver.quit()
        print("Test Completed")
        print(sys.path)

    @allure.title("Login as valid user")
    def test_01_login_valid(self, setup_method):
        driver.get("https://opensource-demo.orangehrmlive.com")

        with allure.step('Open login page'):
            login = LoginPage(driver)
        with allure.step('Insert username'):
            login.enter_username("admin")
        with allure.step('Insert password'):
            login.enter_password("admin123")
        with allure.step('Click submit'):
            login.click_login()
        with allure.step("Get Screenshot"):
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot-Homepage',
                          attachment_type=AttachmentType.PNG)

        homepage = HomePage(driver)
        with allure.step('On Home page click Welcome, a list of links has been opened '):
            homepage.click_welcome()
        with allure.step("Select a Logout link and click to exit the system "):
            homepage.click_logout()
            time.sleep(2)
        with allure.step("Get exit Screenshot"):
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot-Exit', attachment_type=AttachmentType.PNG)

    @allure.title("Invalid login Scenario with wrong username and valid password")
    def test_02_invalid_username(self, setup_method):
        driver.get("https://opensource-demo.orangehrmlive.com")

        with allure.step('Open login page'):
            login = LoginPage(driver)
        with allure.step('Insert invalid username'):
            login.enter_username("admin1")
        with allure.step('Insert password'):
            login.enter_password("admin123")
        with allure.step('Click submit'):
            login.click_login()
        with allure.step("Get Screenshot"):
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot-Homepage',
                          attachment_type=AttachmentType.PNG)
        with allure.step("Validate invalid message"):
            assert "Invalid credentials123" == login.check_invalid_username_message()

    # def test_teardown(self):
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")
