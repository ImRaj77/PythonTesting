import pytest
from pygments.lexer import default
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    # service_obj = Service()  -- Selenium 4 onwards
    # driver = webdriver.Chrome(service=service_obj)
    if browser_name == "chrome":
        driver = webdriver.Chrome("/Users/rajabhau.tidke/Downloads/chrome-driver/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox("/Users/rajabhau.tidke/Downloads/chrome-driver/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()