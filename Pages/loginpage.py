from Locators.locators import Locators

class LoginPage():


    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.userpassword_texbox_id = Locators.userpassword_texbox_id
        self.login_button_name = Locators.login_button_name
        self.invalid_user_name = Locators.invalidUsername_message_xpath


    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.userpassword_texbox_id).clear()
        self.driver.find_element_by_id(self.userpassword_texbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()


    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath(self.invalid_user_name).text
        return msg

