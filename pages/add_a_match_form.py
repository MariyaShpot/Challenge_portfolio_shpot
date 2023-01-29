from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_title_xpath = "//h6[text()='Scouts Panel']"
    main_page_button_xpath = "//div/ul[1]/div[1]"
    players_button_xpath = "//div/ul[1]/div[2]"
    x_player_name_button_xpath = "//div/ul[2]/div[1]"
    matches_button_xpath = "//div/ul[2]/div[2]"
    reports_button_xpath = "//div/ul[2]/div[3]"
    my_team_input_field_xpath = "//*[@name='myTeam']"
    enemy_team_input_field_xpath = "//*[@name='enemyTeam']"
    my_team_score_input_field_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_input_field_xpath = "//*[@name='enemyTeamScore']"
    date_selection_field_xpath = "//*[@name='date']"
    match_at_home_radio_button_xpath = "//*[@name='matchAtHome' and @value='true']"
    match_out_home_radio_button_xpath = "//*[@name='matchAtHome' and @value='false']"
    tshirt_color_input_field_xpath = "//*[@name='tshirt']"
    league_input_field_xpath = "//*[@name='league']"
    time_played_input_field_xpath = "//*[@name='timePlayed']"
    number_input_field_xpath = "//*[@name='number']"
    web_match_input_field_xpath = "//*[@name='webMatch']"
    general_input_field_xpath = "//*[@name='general']"
    rating_input_field_zpath = "//*[@name='rating']"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//div[3]/button[2]"

