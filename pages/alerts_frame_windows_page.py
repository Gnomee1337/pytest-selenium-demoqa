from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self, test_locator):
        available_locators = {
            'new_tab': self.locators.NEW_TAB_BUTTON,
            'new_window': self.locators.NEW_WINDOW_BUTTON
        }
        self.element_is_visible(available_locators[test_locator]).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url
