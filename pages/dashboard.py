from pages.base_page import BasePage

def time_sleep(param):
    pass


class Dashboard(BasePage):

    scouts_panel_title_xpath = "//h6[text()='Scouts Panel']"
    main_page_text_xpath = "//span[text()='Main page']"
    main_page_button_xpath = "//div/ul[1]/div[1]"
    players_text_xpath = "//span[text()='Players']"
    players_button_xpath = "//div/ul[1]/div[2]"
    text_polski_xpath = "//span[text()='Polski']"
    text_english_xpath = "//span[text()='English']"
    language_choice_button_xpath = "//div/ul[2]/div[1]"
    sign_out_text_xpath = "//span[text()='Sign out']"
    sign_out_button_xpath = "//div/ul[2]/div[2]"
    players_count_text_xpath = "//div[text()='Players count']"
    players_count_display_xpath = "//main/div[2]/div[1]"
    matches_count_text_xpath = "//div[text()='Matches count']"
    matches_count_display_xpath = "//main/div[2]/div[2]"
    reports_count_text_xpath = "//div[text()='Reports count']"
    reports_count_display_xpath = "//main/div[2]/div[3]"
    events_count_text_xpath = "//div[text()='Events count']"
    events_count_display_xpath = "//div[2]/div[4]"
    scouts_panel_logo_xpath = "//*[@title='Logo Scouts Panel']"
    player_match_report_management_panel_text_xpath = "//p[text()='Player, match and report management panel.']"
    player_match_report_management_panel_xpath = "//main/div[3]/div[1]/div"
    dev_team_contact_text_xpath = "//span[text()='Dev team contact']"
    dev_team_contact_hyperlink_xpath = "//div[3]/div[1]/div/div[3]/a"
    shortcuts_text_xpath = "//h2[text()='Shortcuts']"
    add_player_text_xpath = "//span[text()='Add player']"
    add_player_button_xpath = "//div[3]/div[2]/div/div/a/button"
    activity_panel_xpath = "//div[3]/div[3]/div"
    activity_text_xpath = "//h2[text()='Activity']"
    last_created_player_text_xpath = "//h6[text()='Last created player']"
    last_updated_player_text_xpath = "//h6[text()='Last updated player']"
    last_created_match_text_xpath = "//h6[text()='Last created match']"
    last_updated_match_text_xpath = "//h6[text()='Last updated match']"
    last_updated_report_text_xpath = "//h6[text()='Last updated report']"
    expected_title = "Scouts panel - sign in"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"

    def title_of_page(self):
        time_sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title







