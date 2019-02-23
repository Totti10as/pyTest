
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = 'txtUsername'
        self.userpassword_texbox_id = 'txtPassword'
        self.login_button_name = "Submit"


    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.userpassword_texbox_id).clear()
        self.driver.find_element_by_id(self.userpassword_texbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()
