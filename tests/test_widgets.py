import random
import time

import allure

from generator.generator import generate_color
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite("Widgets")
class TestWidgets:
    @allure.feature("Accordian Page")
    class TestAccordianPage:
        @allure.title("Check accordian")
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_accordian = accordian_page.check_accordian('first')
            second_accordian = accordian_page.check_accordian('second')
            third_accordian = accordian_page.check_accordian('third')
            assert first_accordian[1] > 1, 'First accordian content doesnt exist'
            assert second_accordian[1] > 1, 'Second accordian content doesnt exist'
            assert third_accordian[1] > 1, 'Third accordian content doesnt exist'

    @allure.feature("Auto Complete Page")
    class TestAutoCompletePage:
        @allure.title("Check fill multi autocomplete")
        def test_fill_multi_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            input_colors = auto_complete_page.fill_input_multi(count=random.randint(1, 11))
            output_colors = auto_complete_page.check_color_in_multi()
            assert input_colors == output_colors

        @allure.title("Check remove value from multi complete")
        def test_remove_value_from_multi_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            input_random_colors = auto_complete_page.fill_input_multi(count=random.randint(1, 11))
            output_length = auto_complete_page.remove_value_from_multi()
            assert output_length[0] == len(input_random_colors) and output_length[1] == len(input_random_colors) - 1

        @allure.title("Check clear all values from multi autocomplete")
        def test_clear_all_values_from_multi_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            input_colors = auto_complete_page.fill_input_multi(count=random.randint(1, 11))
            cleared_result = auto_complete_page.remove_all_elements_from_multi()
            assert len(input_colors) == cleared_result[0] and cleared_result[1] == 0

        @allure.title("Check input in single autocomplete")
        def test_single_input_autocomplete(self, driver):
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()
            input_color = auto_complete_page.fill_input_single()
            output_result = auto_complete_page.check_color_in_single()
            assert input_color[0] == output_result

    @allure.feature("Date Picker Page")
    class TestDatePickerPage:
        @allure.title("Check change date")
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            dates = date_picker_page.select_date()
            assert dates[0] != dates[1], "Date doesnt changed in 'Select Date'"

        @allure.title("Check change date and time")
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            dates = date_picker_page.select_date_and_time()
            print(dates)
            assert dates[0] != dates[1], "Date and time doesnt changed in 'Select Date and Time'"

    @allure.feature("Slider Page")
    class TestSliderPage:
        @allure.title("Check slider")
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            slider_values = slider_page.change_slider_value()
            assert slider_values[0] != slider_values[1], 'Slider value doesnt changed'

    @allure.feature("Progress Bar Page")
    class TestProgressBarPage:
        @allure.title("Check progress bar")
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            progress_bar_data = progress_bar_page.change_progress_bar_value()
            assert progress_bar_data[0] != progress_bar_data[1], "'Progress Bar' value doesnt changed"
        # TODO Add Progress Bar reset after success

    @allure.feature("Tabs Page")
    class TestTabsPage:
        @allure.title("Check tabs")
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            what_data = tabs_page.check_tabs('what')
            origin_data = tabs_page.check_tabs('origin')
            use_data = tabs_page.check_tabs('use')
            assert len(what_data[1]) == 574
            assert len(origin_data[1]) == 763  # 763+295=1058
            assert len(use_data[1]) == 613

    @allure.feature("Tool Tips Page")
    class TestToolTips:
        @allure.title("Check tool tips")
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            tool_tip_text_button, tool_tip_text_field, tool_tip_text_link, tool_tip_number_link = tool_tips_page.check_tool_tips()
            assert tool_tip_text_button == 'You hovered over the Button', "Button tool tip doesnt match"
            assert tool_tip_text_field == 'You hovered over the text field', "Input tool tip doesnt match"
            assert tool_tip_text_link == 'You hovered over the Contrary', "Text Link tool tip doesnt match"
            assert tool_tip_number_link == 'You hovered over the 1.10.32', "NUmber Link tool tip doesnt match"

    @allure.feature("Menu Page")
    class TestMenu:
        @allure.title("Check menu")
        def test_menu(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], 'Menu elements doesnt match'

    # TODO Select Menu
