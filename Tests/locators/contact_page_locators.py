from selenium.webdriver.common.by import By


class Fields_locators:
    contact_form = '//*[@id="pardot-form"]'
    name_input = (By.XPATH, '//*[@id="pardot-form-firstname"]')
    lastname_input = (By.XPATH, '//*[@id="pardot-form-lastname"]')
    email_input = (By.XPATH, '//*[@id="pardot-form-email_address"]')
    company_input = (By.XPATH, '//*[@id="pardot-form-company"]')
    job_title_input = (By.XPATH, '//*[@id="pardot-form-job_title"]')
    area_of_int = (By.XPATH, "//button[@data-id = 'pardot-form-channels']")
    m_dig_spend = (By.XPATH, "//button[@data-id = 'pardot-form-ad_spend']")
    country = (By.XPATH, "//button[@data-id ='pardot-form-country']")
    state = (By.XPATH, "//button[@data-id ='pardot-form-state']")
    questions = (By.XPATH, '//*[@id="pardot-form-comments"]')
    how_heard = (By.XPATH, "//button[@data-id = 'pardot-form-How_Did_You_Hear_About_Us']")
    how_heard_field_other = (By.XPATH, '//*[@id="pardot-form-How_Did_You_Hear_About_Us_Other"]')

    # dropdown_options
    area_of_int_pot_options = "//button[@data-id ='pardot-form-channels']/following-sibling::div/ul/li/a/span[1]"
    m_dig_spend_options = "//button[@data-id ='pardot-form-ad_spend']/following-sibling::div/ul/li/a/span[1]"
    country_option_usa = "//button[@data-id ='pardot-form-country']/following-sibling::div/ul/li[2]/a/span[1]"
    state_options = "//button[@data-id ='pardot-form-state']/following-sibling::div/ul/li/a/span[1]"
    # how_heard_options = "//button[@data-id ='pardot-form-How_Did_You_Hear_About_Us']/following-sibling::div/ul/li/a/span[1]"
    how_heard_options = "//button[@data-id ='pardot-form-How_Did_You_Hear_About_Us']/following-sibling::div/ul/li/a"
    how_heard_option_other = '//button[@data-id="pardot-form-How_Did_You_Hear_About_Us"]/following-sibling::div/ul/li[@data-original-index="9"]'


    # selected_options
    selected_option_area_of_int ="//button[@data-id = 'pardot-form-channels']/span[@class='filter-option pull-left']"
    selected_option_m_dig_spend = "//button[@data-id = 'pardot-form-ad_spend']/span[@class='filter-option pull-left']"
    selected_option_country ="//button[@data-id ='pardot-form-country']/span[@class='filter-option pull-left']"
    selected_option_state = "//button[@data-id ='pardot-form-state']/span[@class='filter-option pull-left']"
    selected_option_how_heard = "//button[@data-id = 'pardot-form-How_Did_You_Hear_About_Us']/span[@class='filter-option pull-left']"


class Button:
    button_contact_us = '//input[@class="form-submit"]'
    # borlabs = "//a[@class='_brlbs-btn _brlbs-btn-accept-all _brlbs-cursor']"
    borlabs = '//*[@id="BorlabsCookieBox"]/div/div/div/div[1]/div/div/div[2]/p[3]/a'


