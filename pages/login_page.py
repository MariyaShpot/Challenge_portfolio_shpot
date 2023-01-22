from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    scouts_panel_title_xpath = "//*[text()='Scouts Panel']"
    remind_password_hyperlink_xpath = "//*[contains(@tabindex, -1)]"
    dropdown_button_xpath = "//*[text()='English' and @role='button']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
