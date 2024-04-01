import base64
import os
import random
import time
from pathlib import Path

import allure
import requests
from selenium.common import TimeoutException

from generator.generator import generated_person, generate_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('check fill all fields')
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    @allure.step('check filled form')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('check open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('check click random checkbox')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        for _ in range(21):
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()

    @allure.step('get checked checkboxes')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element('xpath', self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('get checkbox output result')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('check click on radio button')
    def click_on_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'no': self.locators.NO_RADIOBUTTON
        }
        self.element_is_visible(choices[choice]).click()

    @allure.step('get radio button output result')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('add new person')
    def add_new_person(self, people_count=1):
        for _ in range(people_count):
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('check new added person')
    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for person in person_list:
            if person.text.strip() == '':
                continue
            data.append(person.text.splitlines())
        return data

    @allure.step('search person')
    def search_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('check search person')
    def check_search_person(self, key_word):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        for person in person_list:
            if key_word in person.text.strip():
                return True
        return False

    @allure.step('update person info')
    def update_person_info(self):
        person_info = next(generated_person())
        new_first_name = person_info.first_name
        random_person_update_buttons = self.elements_are_present(self.locators.UPDATE_PERSON_BUTTONS)
        person_update_locator = random_person_update_buttons[
            random.randint(0, len(random_person_update_buttons) - 1)]
        person_update_locator.click()
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).clear()
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(new_first_name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(new_first_name)

    @allure.step('delete person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_PERSON_BUTTONS).click()

    @allure.step('check deleted person')
    def check_deleted_person(self):
        if self.element_is_present(self.locators.NO_ROWS_FOUND).text == "No rows found":
            return True
        else:
            return False

    @allure.step('select up to some rows')
    def select_up_to_some_rows(self):
        row_count_presets = [5, 10, 20, 25, 50, 100]
        data = []
        for row_size in row_count_presets:
            count_row_select = self.choose_select(self.element_is_visible(self.locators.COUNT_ROW_LIST))
            count_row_select.select_by_value(str(row_size))
            data.append(self.check_count_rows())
        return data

    @allure.step('check count rows')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step('click on double button')
    def click_on_double_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.check_clicked_button_result(self.locators.SUCCESS_DOUBLE_TEXT)

    @allure.step('click on right click button')
    def click_on_right_click_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_button_result(self.locators.SUCCESS_RIGHT_TEXT)

    @allure.step('click on click me button')
    def click_on_click_me_button(self):
        click_on_me_button_element = self.element_is_visible(self.locators.CLICK_ME_BUTTON)
        click_on_me_button_element.click()
        return self.check_clicked_button_result(self.locators.SUCCESS_CLICKME_TEXT)

    def check_clicked_button_result(self, element):
        return self.element_is_present(locator=element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step('check new tab simple link')
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        href_link = simple_link.get_attribute('href')
        request = requests.get(href_link)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            if href_link == url:
                return True
            else:
                return False
        else:
            return request.status_code

    @allure.step('check broken link')
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code

    @allure.step('check link status')
    def check_link_status(self, url, expected_code):
        request = requests.get(url)
        request_code = request.status_code
        if request_code == expected_code:
            return True
        else:
            return request_code


class DownloadAndUploadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    @allure.step('upload file')
    def upload_file(self):
        file_name, path = generate_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(file_name)
        uploaded_file_name = file_name.split('\\')[-1]
        uploaded_result_path = self.element_is_present(self.locators.UPLOADED_FILE_RESULT).text
        if uploaded_file_name in uploaded_result_path:
            return True
        else:
            return False

    @allure.step('download file')
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../upload_data'))
        Path(current_dir).mkdir(parents=True, exist_ok=True)
        file_name_path = os.path.join(current_dir, f'downloaded_file_test_{random.randint(1, 999)}.jpeg')
        with open(file_name_path, 'wb+') as downloaded_file:
            offset = link_b.find(b'\xff\xd8')
            downloaded_file.write(link_b[offset:])
            downloaded_file.close()
        check_file = os.path.exists(file_name_path)
        os.remove(file_name_path)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step('check color change')
    def check_color_change(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('check button appearance')
    def check_button_appearance(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON, 5)
        except TimeoutException:
            return False
        return True

    @allure.step('check button is clickable')
    def check_button_is_clickable(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_BUTTON, 5)
        except TimeoutException:
            return False
        return True
