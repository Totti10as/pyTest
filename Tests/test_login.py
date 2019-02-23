from Pages.loginpage import LoginPage
from Pages.homepage import HomePage
from allure_commons.types import AttachmentType
import pytest
import allure
import time



@allure.feature('Login')
@allure.story('Enter into user account')
@allure.severity('blocker')

@pytest.mark.usefixtures("get_driver")
class TestLogin():

    @allure.title("Login as valid user")
    def test_01_login_valid(self, get_driver):

        with allure.step('Open login page'):
            self.login = LoginPage(self.driver)
        with allure.step('Insert username'):
            self.login.enter_username("admin")
        with allure.step('Insert password'):
            self.login.enter_password("admin123")
        with allure.step('Click submit'):
            self.login.click_login()
        with allure.step("Get Screenshot"):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot-Homepage',
                          attachment_type=AttachmentType.PNG)

        homepage = HomePage(self.driver)
        with allure.step('On Home page click Welcome, a list of links has been opened '):
            homepage.click_welcome()
        with allure.step("Select a Logout link and click to exit the system "):
            homepage.click_logout()
            time.sleep(2)
        with allure.step("Get exit Screenshot"):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot-Exit', attachment_type=AttachmentType.PNG)

    @allure.title("Invalid login Scenario with wrong username and valid password")
    def test_02_invalid_username(self, get_driver):

        with allure.step('Open login page'):
            login = LoginPage(self.driver)
        with allure.step('Insert invalid username'):
            login.enter_username("admin1")
        with allure.step('Insert password'):
            login.enter_password("admin123")
        with allure.step('Click submit'):
            login.click_login()
        with allure.step("Get Screenshot"):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot-Homepage',
                          attachment_type=AttachmentType.PNG)
        with allure.step("Validate invalid message"):
            assert "Invalid credentials" == login.check_invalid_username_message()

