class Pardot_locators:
    username = '//*[@id="username"]'
    password = '//*[@id="password"]'
    log_in = '//*[@id="Login"]'
    verification_field = '//*[@id="tc"]'
    save_button = '//*[@id="save"]'
    log_in_sf_button = '//*[@id="logInWithSalesforceButton"]'


class Contact_pardot:
    url_contact = 'https://pi.pardot.com/formHandler/read/id/3667'
    last_lead_link = "(//span[@class='slds']/a)[1]"
    name_field = "(//td[@class ='key' and contains(text(),'Name')]/following-sibling::td[@class ='value breakword'])[1]"
    email_field = "//td[@class='key' and contains(text(),'Email')]/following-sibling::td/span"

    # company_field = "//td[@class='key' and contains(text(), 'Company')]/following-sibling::td/a"
    company_field = "//td[@class='key' and contains(text(), 'Company')]/following-sibling::td"
    job_title_field = "//td[@class='key' and contains(text(), 'Job Title')]/following-sibling::td"
    country_field = "//td[@class='key' and contains(text(), 'Country')]/following-sibling::td"
    state_field = "//td[@class='key' and contains(text(), 'State')]/following-sibling::td"
    channels = "//td[@class='key'][contains(a, 'Channels I am interested in')]/following-sibling::td[@class='value breakword']"
    comment = "//td[@class='key'][contains(a, 'Comment')]/following-sibling::td[@class='value breakword']"
    how_heard = "//td[@class='key'][contains(a, 'How Did You Hear About Us')]/following-sibling::td[@class='value breakword']"
    m_dig_spend = "//td[@class='key'][contains(a, 'My current ad spend')]/following-sibling::td[@class='value breakword']"
    gdpr = "//td[@class='key'][a[text()='GDPR']]/following-sibling::td[@class='value breakword']"
    other = "//td[@class='key'][a[text()='Other (Please Specify)']]/following-sibling::td[@class='value breakword']"
    page_url = "//td[@class='key'][a[text()='Page Url']]/following-sibling::td[@class='value breakword']"


class Form_handler:
    all_leads = "//span[@class='slds']/a[1]"
    #   all_leads = '//*[@id="visitorActivity_view"]/p/label'
