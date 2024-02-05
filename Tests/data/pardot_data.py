import os
class Pardot_data:
      pardot_main = 'https://kenshoo.my.salesforce.com/?ec=302&startURL=%2F&display=page'
      username_data = os.getenv("USERNAME_DATA")
      password_data = os.getenv("PASSWORD_DATA")
      verification_code= ('673129')
      log_in_page = 'https://pi.pardot.com/home/index'
      form_handler_page = 'https://pi.pardot.com/formHandler'

class Contact_page:
      page_url = "/contact-us/"
      gdpr= "Opt-In"
