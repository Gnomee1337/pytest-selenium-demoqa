import random
import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
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


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_will_appear_alert(self):
        self.element_is_visible(self.locators.WILL_APPEAR_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_BUTTON_RESULT).text
        return text_result

    def check_prompt_alert(self):
        test_input = f'test-input{random.randint(0, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(test_input)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_BUTTON_RESULT).text
        return text_result, test_input


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_number):
        possible_frames = {
            'frame_1': self.locators.FIRST_FRAME,
            'frame_2': self.locators.SECOND_FRAME,
        }
        frame = self.element_is_present(possible_frames[frame_number])
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        frame_text = self.element_is_present(self.locators.TITLE_FRAME).text
        self.driver.switch_to.default_content()
        return [frame_text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_tested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text

        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_small_modal_dialog(self):
        self.element_is_visible(self.locators.SMALL_MODAL_DIALOG_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        body_small = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        if title_small == 'Small Modal' and len(body_small) == 47:
            return True
        else:
            return False

    def check_large_modal_dialog(self):
        self.element_is_visible(self.locators.LARGE_MODAL_DIALOG_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        body_large = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        if title_large == 'Large Modal' and len(body_large) == 574:
            return True
        else:
            return False
