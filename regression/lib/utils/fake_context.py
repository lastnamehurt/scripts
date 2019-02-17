from selenium import webdriver

from scripts.regression.lib.utils.constants import URL


class FakeContext:
    pass


context = FakeContext()
context.browser = webdriver.Chrome()
context.base_url = URL.TWITTER
