from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    web_url = "https://ndosisimplifiedautomation.vercel.app/"
    home_login_button_xpath = "//span[normalize-space()='Login']"
    username_id_textbox = "login-email"
    password_id_textbox = "login-password"
    login_submit_button_id = "login-submit"
    verify_dashboard = "//h2"

    def test_login(self):
        #start the driver and launch the website
        self.driver = webdriver.Chrome()
        self.driver.get(self.web_url)

        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located((By.XPATH, self.home_login_button_xpath))).click()
        #wait.until(EC.visibility_of_element_located((By.ID, self.username_id_textbox))).send_keys("melomazibuko8@gmail.com")
        self.driver.find_element(By.ID, self.username_id_textbox).send_keys("melomazibuko8@gmail.com")
        self.driver.find_element(By.ID, self.password_id_textbox).send_keys("Mwelase@1031")
        self.driver.find_element(By.ID, self.login_submit_button_id).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, self.verify_dashboard))).is_displayed()

        self.driver.close()






