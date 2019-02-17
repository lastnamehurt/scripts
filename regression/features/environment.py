import logging
import os
import time

import yaml
from behave import use_step_matcher
from selenium import webdriver

from regression.lib.utils.constants import Path

use_step_matcher("re")


def before_all(context):
    context.logger = logging

    # import config settings
    with open(os.getcwd() + os.path.sep + Path.CONFIG, 'r') as ymlfile:
        context.config = yaml.safe_load(ymlfile)
    context.browser = context.config.get('env')['browser']
    if context.browser == 'chrome':
        context.browser = webdriver.Chrome()
    else:
        raise RuntimeError("Please run with Chrome")
    if not os.path.exists(Path.FAILED_SCREENSHOT):
        os.makedirs(Path.FAILED_SCREENSHOT)
    context.twitter_username = context.config.get('userdata')['username']
    if not context.twitter_username:
        context.twitter_username = os.environ.get("TWITTER_USERNAME")
    context.twitter_password = context.config.get('userdata')['password']
    if not context.twitter_password:
        context.twitter_password = os.environ.get("TWITTER_PASSWORD")


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    if scenario.status == "failed":
        print("Failed: {}".format(Path.FAILED_SCREENSHOT + scenario.name + "_failed.png"))
        context.logger.info("Failed: {}".format(Path.FAILED_SCREENSHOT + scenario.name + "_failed.png"))
        context.browser.save_screenshot(Path.FAILED_SCREENSHOT + scenario.name + "_failed.png")
    context.browser.delete_all_cookies()


def after_feature(context, feature):
    context.browser.quit()


def after_all(context):
    pass
