import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    print('\nParser begin')
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nStart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser...")
    browser.quit()
    
 


