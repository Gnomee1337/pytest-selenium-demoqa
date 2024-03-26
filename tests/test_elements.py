import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    DownloadAndUploadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "input_data doesnt match output_data in Text Box"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_data = check_box_page.get_checked_checkboxes()
            output_data = check_box_page.get_output_result()
            assert input_data == output_data, 'selected checkboxes doesnt match in Check Box'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no != 'No', "'No' have been selected"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, "'new_person' not found in web table"

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            person_found = web_table_page.check_search_person(
                new_person[random.randint(0, len(new_person) - 1)])
            assert person_found, "'person_found' not found in web table by search key_word"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            update_info = web_table_page.update_person_info()
            found_updated_person = web_table_page.check_search_person(update_info)
            assert found_updated_person, "'updated person' not found in web table"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person_email = web_table_page.add_new_person()[3]
            web_table_page.search_person(new_person_email)
            web_table_page.delete_person()
            person_deleted = web_table_page.check_deleted_person()
            assert person_deleted, "'deleted person' found in web table"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            rows_count = web_table_page.select_up_to_some_rows()
            assert rows_count == [5, 10, 20, 25, 50, 100], "The 'rows count' doesnt match in web table"

    class TestButtonsPage:
        def test_different_click_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            assert buttons_page.click_on_double_button(), "'Double click button' haven't been clicked"
            assert buttons_page.click_on_right_click_button(), "'Right click button' haven't been clicked"
            assert buttons_page.click_on_click_me_button(), "'Click me button' haven't been clicked"

    class TestLinksPage:
        def test_check_links(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            assert links_page.check_new_tab_simple_link(), "'Home' link doesnt match the href url"

        def test_broken_links(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad_request')
            assert response_code == 400

        def test_all_api_calls(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            assert links_page.check_link_status(url='https://demoqa.com/created',
                                                expected_code=201), "'Created' link doesnt match the 201 status code"
            assert links_page.check_link_status(url='https://demoqa.com/no-content',
                                                expected_code=204), "'No Content' link doesnt match the 204 status code"
            assert links_page.check_link_status(url='https://demoqa.com/moved',
                                                expected_code=301), "'Moved' link doesnt match the 301 status code"
            assert links_page.check_link_status(url='https://demoqa.com/bad-request',
                                                expected_code=400), "'Bad Request' link doesnt match the 400 status code"
            assert links_page.check_link_status(url='https://demoqa.com/unauthorized',
                                                expected_code=401), "'Unauthorized' link doesnt match the 401 status code"
            assert links_page.check_link_status(url='https://demoqa.com/forbidden',
                                                expected_code=403), "'Forbidden' link doesnt match the 403 status code"
            assert links_page.check_link_status(url='https://demoqa.com/invalid-url',
                                                expected_code=404), "'Not Found' link doesnt match the 404 status code"

    class TestUploadAndDownloadPage:
        def test_upload_file(self, driver):
            download_upload_page = DownloadAndUploadPage(driver, "https://demoqa.com/upload-download")
            download_upload_page.open()
            assert download_upload_page.upload_file(), "Uploaded file has not been uploaded 'C:\fakepath'"

        def test_download_file(self, driver):
            download_upload_page = DownloadAndUploadPage(driver, "https://demoqa.com/upload-download")
            download_upload_page.open()
            assert download_upload_page.download_file(), 'Downloaded file has not been downloaded'

    class TestDynamicProperties:
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            button_is_enabled = dynamic_properties_page.check_button_is_clickable()
            assert button_is_enabled, "'Will enable' button is not clickable"

        def test_color_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_color_change()
            assert color_before != color_after, "'Color Change' button doesnt change color"

        def test_visible_after_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            button_appears = dynamic_properties_page.check_button_appearance()
            assert button_appears, "'Visible after' button doesnt appear"
