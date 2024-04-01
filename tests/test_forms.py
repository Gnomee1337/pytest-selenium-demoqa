import time

import allure

from pages.forms_page import FormsPage


@allure.suite("Forms")
class TestForms:
    @allure.feature("Forms Page")
    class TestFormsPage:
        @allure.title("Check form")
        def test_form(self, driver):
            forms_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
            forms_page.open()
            filled_info = forms_page.fill_form_fields()
            results = forms_page.forms_result()
            # TODO Verify every field
            assert results[1] in filled_info, 'Filled form info doesnt match result'
