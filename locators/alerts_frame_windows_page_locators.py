from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button#tabButton')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')