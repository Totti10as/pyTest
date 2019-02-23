from selenium import webdriver

import time
import pytest
import allure
from Pages.loginpage import LoginPage
from allure_commons.types import AttachmentType
import sys



class TestLoign():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(
            executable_path='C:/Users/Totti10/PycharmProjects/POMProcject/drivers/chromedriver.exe')
        driver.implicitly_wait(10)
        driver.set_window_size(1200, 800)
        yield
        time.sleep(5)
        driver.close()
        driver.quit()
        print("Test Completed")
        print(sys.path)

    @allure.feature('Login')
    @allure.story('Enter into user account')
    @allure.severity('blocker')
    def test_login_valid(self, test_setup):
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
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

        # homepage = HomePage(driver)
        # homepage.click_welcome()
        # homepage.click_logout()
        # time.sleep(2)

        # driver.find_element_by_id("txtUsername").send_keys("admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_name("Submit").click()
        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()

    # def test_teardown(self):
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")
