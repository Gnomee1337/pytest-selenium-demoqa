import random

from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div#section1Heading')
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, 'div#section1Content p')

    SECTION_SECOND = (By.CSS_SELECTOR, 'div#section2Heading')
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, 'div#section2Content p')

    SECTION_THIRD = (By.CSS_SELECTOR, 'div#section3Heading')
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, 'div#section3Content p')


class AutoCompletePageLocators:
    MULTIPLE_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteMultipleInput')
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTIPLE_REMOVE_BUTTON = (By.CSS_SELECTOR, 'div#autoCompleteMultipleContainer svg path')
    MULTI_CLEAR_ALL_BUTTON = (By.CSS_SELECTOR, 'div.auto-complete__clear-indicator svg path')

    SINGLE_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteSingleInput')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input#datePickerMonthYearInput')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select.react-datepicker__month-select')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select.react-datepicker__year-select')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day--"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input#dateAndTimePickerInput')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div.react-datepicker__month-read-view')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__month-option')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div.react-datepicker__year-read-view')
    DATE_AND_TIME_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day--']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__year-option')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li.react-datepicker__time-list-item ')


class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input#sliderValue')


class ProgressBarPageLocators:
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[role='progressbar']")
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button#startStopButton')
    PROGRESS_RESET_BUTTON = (By.CSS_SELECTOR, 'button#resetButton')


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, 'a#demo-tab-what')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-what p')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'a#demo-tab-origin')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-origin p')
    TABS_USE = (By.CSS_SELECTOR, 'a#demo-tab-use')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-use p')
    TABS_MORE = (By.CSS_SELECTOR, 'a#demo-tab-more')


class ToolTipsPageLocators:
    HOVER_BUTTON = (By.CSS_SELECTOR, 'button#toolTipButton')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    HOVER_INPUT = (By.CSS_SELECTOR, 'input#toolTipTextField')
    TOOL_TIP_INPUT = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    HOVER_LINK_TEXT = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_LINK_TEXT = (By.XPATH, '//*[@aria-describedby="contraryTexToolTip"]')

    HOVER_LINK_NUMBER = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIL_LINK_NUMBER = (By.XPATH, '//*[@aria-describedby="sectionToolTip"]')

    TOOL_TIP_INNERS = (By.CSS_SELECTOR, 'div.tooltip-inner')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul#nav li a')
