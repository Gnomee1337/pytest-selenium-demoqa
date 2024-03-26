from pages.alerts_frame_windows_page import BrowserWindowsPage


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
