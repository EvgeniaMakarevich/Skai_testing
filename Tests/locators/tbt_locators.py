from selenium.webdriver.common.by import By


class ContactForm:
    scroll_to_form = (By.XPATH, '//*[@id="the_big_shift"]/div/div/div/div[7]/a/span[1]')
    button_modal_window = (By.XPATH, '//*[@id="expert-voices"]/div/div/div/div[1]/div/div[1]/div/div/a/span[1]')
    modal_window = (By.XPATH,"//div[@id = 'contact-form']/div/div[@class = 'kt-modal-container kt-modal-height-fittocontent kt-close-position-inside']")

    # fields
    first_name_field = (By.XPATH, "//input[@id = 'input_2_5']")
    last_name_field = (By.XPATH, "//input[@id = 'input_2_7']")
    email_address_field = (By.XPATH, "//input[@id = 'input_2_8']")
    message_field = (By.XPATH, "//textarea[@id = 'input_2_9']")
    submit_button = (By.XPATH, "//button[@id = 'gform_submit_button_2']")
