import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Pet Store'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nilesh'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
