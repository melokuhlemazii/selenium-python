from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    web_url = "https://ndosisimplifiedautomation.vercel.app/"
    home_login_button_xpath = "//span[normalize-space()='Login']"
    username_id_textbox = "login-email"
    password_id_textbox = "login-password"
    login_submit_button_id = "login-submit"

    def test_login(self):
        #start the driver and launch the website
        self.driver = webdriver.Chrome()
        self.driver.get(self.web_url)

        wait = WebDriverWait(self.driver, 10)








