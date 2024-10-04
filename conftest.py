from selenium import webdriver
import pytest
import time


# only fixture
# @pytest.fixture(params=["chrome","edge"])
# def prasad(request):
#     global driver
#
#     if request.param=="chrome":
#         driver = webdriver.Chrome()
#     elif request.param=="edge":
#         driver=webdriver.Edge()
#     driver.get("https://www.instagram.com/accounts/login/?hl=en")
#     driver.implicitly_wait(10)
#     request.cls.driver=driver
#
#     yield
#
#     time.sleep(5)
#     driver.quit()


# browser from command prompt and fixture
@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield

    time.sleep(5)
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
