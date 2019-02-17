from __future__ import unicode_literals

from regression.lib.locators.login import LoginLocators
from regression.lib.page_objects.base_page import BasePage
from regression.lib.page_objects.twitter_timeline import TwitterTimeline
from regression.lib.utils.constants import URL


class LoginPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self,
                          context.browser,
                          )
        self.context = context
        self.base_url = URL.TWITTER
        self.visit(url=self.base_url)

    locator_dictionary = LoginLocators.__dict__

    def login(self, username='', password=''):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.submit_btn.click()
        return TwitterTimeline(self.context)
