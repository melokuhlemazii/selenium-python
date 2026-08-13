from Pages.login_page import LoginPage
from Pages.home_page import HomePage


def login(driver, username, password):
    homeeePage = HomePage(driver)
    loginnPage = LoginPage(driver)

    homeeePage.clickLoginButton()
    loginnPage.getUsername(username)
    loginnPage.getPassword(password)
    loginnPage.getLoginButton()

