from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    scouts_panel_title_xpath = "//*[text()='Scouts Panel']"
    remind_password_hyperlink_xpath = "//div/div[1]/a"
    dropdown_button_xpath = "//*[text()='English' and @role='button']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def fill_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_the_button(self, click):
        self.click_on_the_element(self.sign_in_button_xpath, click)
