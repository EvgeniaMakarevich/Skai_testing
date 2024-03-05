from selenium.webdriver.common.by import By
class EventFormLocators:
    # form_1
    first_name = (By.XPATH, "//input[@id = 'pardot-form-firstname']")
    last_name = (By.XPATH, "//input[@id = 'pardot-form-lastname']")
    email = (By.XPATH, "//input[@id = 'pardot-form-email_address']")
    phone = (By.XPATH, "//input[@id = 'pardot-form-phone']")
    company = (By.XPATH, "//input[@id = 'pardot-form-company']")
    job_title = (By.XPATH, "//input[@id = 'pardot-form-job_title']")
    country = (By.XPATH, "//button[@data-id ='pardot-form-country']")
    state = (By.XPATH, "//button[@data-id ='pardot-form-state']")
    dietary_req = (By.XPATH, "//input[@id = 'pardot-form-dietary_requirements']")

    # form_2
    what_interested_in = (By.XPATH, "//button[@data-id ='pardot-form-who_would_you_like_to_meet']")
    what_to_discuss = (By.XPATH, "//input[@id = 'pardot-form-what_would_you_like_to_discuss']")

    # ---------------------

    # dropdown_options
    # form_1
    country_option_usa = "//button[@data-id ='pardot-form-country']/following-sibling::div/ul/li[2]/a/span[1]"
    state_options = "//button[@data-id ='pardot-form-state']/following-sibling::div/ul/li/a/span[1]"

    # form_2
    what_interested_in_options = "//button[@data-id ='pardot-form-who_would_you_like_to_meet']/following-sibling::div/ul/li/a/span[1]"

    # --------------------

    # selected_options
    # form_1
    selected_option_country = "//button[@data-id ='pardot-form-country']/span[@class='filter-option pull-left']"
    selected_option_state = "//button[@data-id ='pardot-form-state']/span[@class='filter-option pull-left']"

    # form_2
    selected_option_what_interested_in = "//button[@data-id ='pardot-form-who_would_you_like_to_meet']/span[@class='filter-option pull-left']"

    # --------------------


    # checkbox
    privacy_policy = "//label[@for = 'pardot-form-agreed_privacy_policy']"
    contact_me = "//label[@for = 'pardot-form-agreed_legal_language']"

    # button
    submit_button = "//input[@class= 'form-submit']"


    #form
    form_locator = '//*[@id="pardot-form"]'



