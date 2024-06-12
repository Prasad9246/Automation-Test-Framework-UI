import pytest
from selenium import webdriver
from excelDataProvider.readExcelData import ReadExcelData
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


@pytest.fixture
def init_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()


@pytest.fixture(
    params=ReadExcelData("C:/Users/Prasad Kamble/OneDrive - chiacon.com/Documents/web selenium interface/version6/testData/testData.xlsx").read_data(
        "Login_Page"))
def test_data(request):
    return request.param
