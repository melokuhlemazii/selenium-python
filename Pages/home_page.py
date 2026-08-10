from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    main_login_button_xpath = "//span[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def getLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element_by_xpath(self.main_login_button_xpath)).click()

