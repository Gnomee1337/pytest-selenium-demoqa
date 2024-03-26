import os

from selenium.webdriver import Keys
from selenium.webdriver.common import keys

from generator.generator import generated_person, generate_file
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage


class FormsPage(BasePage):
    locators = FormsPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generate_file()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.phone_number)
        # TODO ADD date_of_birth
        self.element_is_visible(self.locators.SUBJECTS).send_keys("Maths")  # TODO Modify to random subject
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.PICTURE).send_keys(path)
        os.remove(file_name)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()  # TODO Modify to random state
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_present(self.locators.SELECT_CITY))
        self.element_is_visible(self.locators.SELECT_CITY).click()  # TODO Modify to random city
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_present(self.locators.SUBMIT_BUTTON))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person

    def forms_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        found_results = []
        for item in result_list:
            found_results.append(item.text)
        return found_results
