import time

from behave import *

from regression.lib.page_objects.login import LoginPage
from regression.lib.utils.constants import USER_MAP, Constants, URL

from hamcrest import assert_that, contains_string, equal_to

use_step_matcher("re")


@given("twitters homepage")
def step_load_twitter(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page = LoginPage(context)
    assert_that(context.login_page.browser.current_url, contains_string(URL.TWITTER))
    assert_that(context.login_page.username.get_attribute('autocomplete'), equal_to(Constants.USERNAME))
    time.sleep(4)


@when('"(?P<user>.+)" logs in')
def step_login(context, user):
    """
    :type context: behave.runner.Context
    :type user: str
    """
    context.timeline_page = context.login_page.login(username=context.twitter_username, password=context.twitter_password)
    time.sleep(3)
    assert_that(context.timeline_page.avatar.get_attribute('title'), equal_to("Profile and settings"))


@then("the twitter timeline appears")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.timeline_page.view_latest_tweets(search=True)
    time.sleep(3)
    assert_that(context.timeline_page.browser.current_url, contains_string(Constants.TWEETS))
