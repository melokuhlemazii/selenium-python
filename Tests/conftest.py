#similar to browser factory
from selenium import webdriver

def setup(browser):
    #initialize the webdriver based on the browser name provided
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "edge":
        driver = webdriver.Edge()

    elif browser.lower() == "safari":
        driver = webdriver.Safari()

    else:
        driver = webdriver.Firefox()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
