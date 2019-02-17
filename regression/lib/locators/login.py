from selenium.webdriver.common.by import By


class LoginLocators:
    username = (By.NAME, "session[username_or_email]")
    password = (By.NAME, "session[password]")
    submit_btn = (By.CLASS_NAME, "js-submit")
