import pytest
import time
from selenium import webdriver


def test_add_to_basket_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(30)
    elem = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(elem) == 1