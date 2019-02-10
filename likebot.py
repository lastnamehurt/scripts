import os
import random
import time
import traceback

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class URL:
    TWITTER = 'http://twitter.com'


class Constants:
    USERNAME = os.environ.get("TWITTER_USERNAME")
    PASSWORD = os.environ.get("TWITTER_PASSWORD")
    GLOBAL_ENTRY_Q = '#globalentry'


class TwitterLocator:
    username = (By.NAME, "session[username_or_email]")
    password = (By.NAME, "session[password]")
    submit_btn = (By.CLASS_NAME, "js-submit")
    search_input = (By.ID, "search-query")
    search_btn = (By.ID, "nav-search")
    tweets = (By.CLASS_NAME, "js-stream-item")
    like_btn = (By.CLASS_NAME, "HeartAnimation")
    latest_tweets = (By.PARTIAL_LINK_TEXT, 'Latest')


class LikeBot(object):

    def __init__(self):
        self.locator_dictionary = TwitterLocator.__dict__
        self.browser = webdriver.Chrome()  # export PATH=$PATH:/path/to/chromedriver/folder
        self.browser.get(URL.TWITTER)
        self.timeout = 10

    def login(self, username=Constants.USERNAME, password=Constants.PASSWORD):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.submit_btn.click()

    def search(self, q=Constants.GLOBAL_ENTRY_Q):
        self.search_input.send_keys(q)
        self.search_input.send_keys(Keys.ENTER)

    def view_latest_tweets(self):
        self.latest_tweets.click()

    def like_tweet(self):
        """
        Like a random tweet
        :return:
        """
        tweets = self.browser.find_elements(*self.locator_dictionary['tweets'])
        tweet = random.choice(tweets)
        like = tweet.find_element(*self.locator_dictionary['like_btn'])
        like.click()
        print("Liked Tweet: {}".format(tweet.text))

    def _find_element(self, *loc):
        return self.browser.find_element(*loc)

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
                return self._find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(LikeBot, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print "No %s here!" % what

    def run(self):
        self.login()
        self.search()
        self.view_latest_tweets()
        time.sleep(2)
        self.like_tweet()
        self.browser.quit()

if __name__ == "__main__":
    LikeBot().run()