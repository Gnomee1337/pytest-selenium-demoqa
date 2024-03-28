import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            new_tab_url = new_tab_page.check_opened_new_tab('new_tab')
            assert new_tab_url == 'https://demoqa.com/sample', "'New tab' window doesnt match expected url"

        def test_new_window(self, driver):
            test_new_window = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            test_new_window.open()
            new_window_url = test_new_window.check_opened_new_tab('new_window')
            assert new_window_url == 'https://demoqa.com/sample', "'New window' window doesnt match expected url"

    class TestAlerts:
        def test_see_alert(self, driver):
            test_see_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            test_see_alert.open()
            see_alert_text = test_see_alert.check_see_alert()
            assert see_alert_text == 'You clicked a button'

        def test_will_appear_alert(self, driver):
            test_will_appear_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            test_will_appear_alert.open()
            will_appear_alert_text = test_will_appear_alert.check_will_appear_alert()
            assert will_appear_alert_text == 'This alert appeared after 5 seconds'

        def test_confirm_alert(self, driver):
            test_confirm_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            test_confirm_alert.open()
            confirm_alert_text = test_confirm_alert.check_confirm_alert()
            assert confirm_alert_text == 'You selected Ok'

        def test_prompt_alert(self, driver):
            test_prompt_alert = AlertsPage(driver, "https://demoqa.com/alerts")
            test_prompt_alert.open()
            confirm_alert_text, test_input = test_prompt_alert.check_prompt_alert()
            assert confirm_alert_text == f'You entered {test_input}'

    class TestFrames:
        def test_frames(self, driver):
            frame_page = FramesPage(driver, "https://demoqa.com/frames")
            frame_page.open()
            frame_1_result = frame_page.check_frame('frame_1')
            assert frame_1_result == ['This is a sample page', '500px', '350px'], 'The frame1 does not exist'
            frame_2_result = frame_page.check_frame('frame_2')
            assert frame_2_result == ['This is a sample page', '100px', '100px'], 'The frame2 does not exist'

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_tested_frame()
            assert parent_text == 'Parent frame', 'Nested Parent frame does not exist'
            assert child_text == 'Child Iframe', 'Nested Child frame does not exist'

    class TestModalDialogs:
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            assert modal_dialogs_page.check_small_modal_dialog(), 'Small Modal doesnt match'
            assert modal_dialogs_page.check_large_modal_dialog(), 'Large Modal doesnt match'
