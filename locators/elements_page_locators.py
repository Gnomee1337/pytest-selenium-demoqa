from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # Created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button.rct-option-expand-all')
    ITEM_LIST = (By.CSS_SELECTOR, 'span.rct-title')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg.rct-icon-check.rct-icon')
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span.text-success')


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span.text-success')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button#addNewRecordButton')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input#firstName')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, 'input#age')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input#department')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#submit.btn-primary')

    # tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div.rt-tr-group')
    DELETE_PERSON_BUTTONS = (By.CSS_SELECTOR, 'span[id^="delete-record-"]')
    UPDATE_PERSON_BUTTONS = (By.CSS_SELECTOR, 'span[id^="edit-record-"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div.rt-noData')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # search_box
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input#searchBox')