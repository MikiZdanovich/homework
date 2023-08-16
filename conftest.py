import os

import pytest
from src.utils.webdriver_manager import DriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="Type of web driver: chrome, firefox, or edge",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run tests in headless mode",
        default=True,
    )


@pytest.fixture(scope="function")
def driver(request):
    is_headless = request.config.getoption("--headless")

    driver_name = (
        request.config.getoption("driver") or os.getenv("WEBDRIVER", "chrome").lower()
    )
    _driver = DriverManager.get_driver(driver_name, is_headless)
    yield _driver
    _driver.quit()
