import pytest

from pytest_bdd import scenarios, given, when, then, parsers, scenario
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class pagedetails():
    '''created a blank class to store saved attributes during webscrapping'''
    pass

# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()


@pytest.fixture
def page():
    p= pagedetails()
    yield p





# Given Steps

@given(parsers.parse('go to {homepage}'))
def ddg_home(browser, homepage):
    browser.get(homepage)


# When Steps

@when(parsers.parse('the user finds element with name - {elementname}'))
def search_element(browser, page, elementname):
    page.currentelement = browser.find_element_by_name(elementname)


@when(parsers.parse('the user finds element with id - {elementid}'))
def search_element(browser, page, elementid):
    page.currentelement = browser.find_element_by_id(elementid)


@when(parsers.parse('the user finds element with class - {elementclass}'))
def search_element(browser, elementclass):
    page.currentelement = browser.find_element_by_class_name(elementclass)


@when(parsers.parse('the user enters <phrase> in element'))
def enter_phrase(browser,page, phrase):
    page.currentelement.send_keys(phrase)


@when(parsers.parse('the user enters returnkey in element'))
def enter_phrase(browser,page):
    page.currentelement.send_keys(Keys.ENTER)


@when(parsers.parse('the user clicks the element'))
def search_phrase(browser,page):
    page.currentelement.click()


@when(parsers.parse('get the attribute {attributeName} of the element to {variablename} variable'))
def search_phrase(browser,page, attributeName,variablename):
    page.__dict__[variablename]=page.currentelement.get_attribute(attributeName)


@when(parsers.parse('get the text of the element to {variablename} variable'))
def search_phrase(browser,page, variablename):
    page.__dict__[variablename]=page.currentelement.text[0:500]


@then(parsers.parse('save <phrase> {variablename} to {filename} file'))
def search_results(browser,page,variablename,phrase,filename):
    f = open(filename, "a+")
    f.write(phrase + ',"' + page.__dict__[variablename] + '"\n')
    f.close()

