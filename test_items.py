import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_add_to_basket_btn_presents(browser):
    print('\nTest_begins')
    browser.get(link)
    time.sleep(30)
    browser.implicitly_wait(5)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "No such element"