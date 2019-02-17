from selenium.webdriver.common.by import By


class TwitterLocator:
    search_input = (By.ID, "search-query")
    search_btn = (By.ID, "nav-search")
    tweets = (By.CLASS_NAME, "js-stream-item")
    like_btn = (By.CLASS_NAME, "HeartAnimation")
    latest_tweets = (By.PARTIAL_LINK_TEXT, 'Latest')
    avatar = (By.ID, "user-dropdown-toggle")