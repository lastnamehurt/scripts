from __future__ import absolute_import

# Put Standard Library Imports Here:
import contextlib
import time
import traceback

# Put Third Party/Django Imports Here:
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """
    Really the only method used here is '__getattr__' now
    """

    def __init__(self, browser, base_url='', **kwargs):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 10

    @contextlib.contextmanager
    def wait_for_page_load(self, timeout=10):
        old_page = self.find_element_by_tage_name('html')
        yield
        WebDriverWait(self, timeout).until(staleness_of(old_page))

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def visit(self, url='', route=''):
        if not url:
            url = self.base_url
        self.browser.get(url + route)

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()
        # I don't like this but hover is sensitive and needs some sleep time
        time.sleep(5)

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print "No %s here!" % what
