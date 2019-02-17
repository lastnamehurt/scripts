import random
import time

from selenium.webdriver.common.keys import Keys

from regression.lib.locators.twitter import TwitterLocator
from regression.lib.page_objects.base_page import BasePage
from regression.lib.utils.constants import URL, Constants


class TwitterTimeline(BasePage):
    locator_dictionary = TwitterLocator.__dict__

    def __init__(self, context):
        BasePage.__init__(self,
                          context.browser,
                          )
        self.context = context
        self.base_url = URL.TWITTER
        self.visit(url=self.base_url)

    def search(self, q=Constants.GLOBAL_ENTRY_Q):
        self.search_input.send_keys(q)
        self.search_input.send_keys(Keys.ENTER)

    def view_latest_tweets(self, search=False):
        if search:
            self.search()
            time.sleep(2)
        self.latest_tweets.click()

    def like_tweet(self):
        tweets = self.context.browser.find_elements(*self.locator_dictionary['tweets'])
        tweet = random.choice(tweets)
        like = tweet.find_element(*self.locator_dictionary['like_btn'])
        like.click()
