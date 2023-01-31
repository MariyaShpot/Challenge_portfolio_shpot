from _pytest import unittest
from selenium.webdriver.chrome import webdriver

from pages.add_a_player import click_on_the_add_player_button
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_match_form import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

import os
import time
import unittest
from selenium import webdriver


class TestAddAPlayer(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self, dashboard_page='Dashboard', add_a_player_page='add_player_url'):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user08@getnada.com')
        user_login.fill_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)
        user_login.dashboard_page = Dashboard(self.driver)
        time.sleep(5)
        click_on_the_add_player_button(self)
        time.sleep(5)
        add_a_player_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()