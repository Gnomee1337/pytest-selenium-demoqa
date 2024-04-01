import random
import time

import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generate_color, generate_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step('check accordian')
    def check_accordian(self, accordian_num):
        accordians = {
            'first': {'title': self.locators.SECTION_FIRST, 'content': self.locators.SECTION_FIRST_CONTENT},
            'second': {'title': self.locators.SECTION_SECOND, 'content': self.locators.SECTION_SECOND_CONTENT},
            'third': {'title': self.locators.SECTION_THIRD, 'content': self.locators.SECTION_THIRD_CONTENT},
        }
        section_title = self.element_is_visible(accordians[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordians[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step('fill input multi')
    def fill_input_multi(self, count=1):
        colors = random.sample(next(generate_color()).color_name, k=count)
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTIPLE_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('fill input single')
    def fill_input_single(self):
        color = random.sample(next(generate_color()).color_name, k=1)
        input_single = self.element_is_visible(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color

    @allure.step('remove value from multi')
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTIPLE_REMOVE_BUTTON)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return [count_value_before, count_value_after]

    @allure.step('remove all elements from multi')
    def remove_all_elements_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        self.element_is_visible(self.locators.MULTI_CLEAR_ALL_BUTTON).click()
        try:
            count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        except TimeoutException:
            count_value_after = 0
        return [int(count_value_before), int(count_value_after)]

    @allure.step('check color in multi')
    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('check color in single')
    def check_color_in_single(self):
        color = self.element_is_present(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('select date')
    def select_date(self):
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('select date and time')
    def select_date_and_time(self):
        date_and_time = next(generate_date())
        input_date_and_time = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_and_time_before = input_date_and_time.get_attribute('value')
        input_date_and_time.click()
        # Month
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date_and_time.month)
        # Year
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        # Day
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_DAY_LIST, date_and_time.day)
        # Time
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date_and_time.time)
        value_date_and_time_after = input_date_and_time.get_attribute('value')
        return value_date_and_time_before, value_date_and_time_after

    @allure.step('set date by text')
    def set_date_by_text(self, element, value):
        select = self.choose_select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('set date item from list')
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('change slider value')
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step('change progress bar value')
    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar_button = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1, 5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('check tabs')
    def check_tabs(self, tab_name):
        tabs = {
            'what': {'title': self.locators.TABS_WHAT, 'content': self.locators.TABS_WHAT_CONTENT},
            'origin': {'title': self.locators.TABS_ORIGIN, 'content': self.locators.TABS_ORIGIN_CONTENT},
            'use': {'title': self.locators.TABS_USE, 'content': self.locators.TABS_USE_CONTENT},
            'more': {'title': self.locators.TABS_MORE, 'content': 0},
        }
        cur_button = self.element_is_visible(tabs[tab_name]['title'])
        try:
            cur_button.click()
        except ElementClickInterceptedException:
            pass
        tab_content = self.element_is_visible(tabs[tab_name]['content']).text
        return [cur_button.text, tab_content]


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step('get text from tool tips')
    def get_text_from_tool_tips(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        time.sleep(0.5)
        self.element_is_visible(wait_element)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIP_INNERS).text
        return tool_tip_text

    @allure.step('check tool tips')
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.HOVER_BUTTON, self.locators.TOOL_TIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.HOVER_INPUT, self.locators.TOOL_TIP_INPUT)
        tool_tip_text_link = self.get_text_from_tool_tips(self.locators.HOVER_LINK_TEXT,
                                                          self.locators.TOOL_TIP_LINK_TEXT)
        tool_tip_number_link = self.get_text_from_tool_tips(self.locators.HOVER_LINK_NUMBER,
                                                            self.locators.TOOL_TIL_LINK_NUMBER)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_link, tool_tip_number_link


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('check menu')
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
