from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button#tabButton')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#alertButton')
    WILL_APPEAR_BUTTON = (By.CSS_SELECTOR, 'button#timerAlertButton')
    CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, 'button#confirmButton')
    PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, 'button#promtButton')

    CONFIRM_BUTTON_RESULT = (By.CSS_SELECTOR, 'span#confirmResult')
    PROMPT_BUTTON_RESULT = (By.CSS_SELECTOR, 'span#promptResult')


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe#frame1')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe#frame2')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1#sampleHeading')


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe#frame1')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL_DIALOG_BUTTON = (By.CSS_SELECTOR, 'button#showSmallModal')
    LARGE_MODAL_DIALOG_BUTTON = (By.CSS_SELECTOR, 'button#showLargeModal')

    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div.modal-body')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, 'div.modal-body p')

    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-sm')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-lg')

    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button#closeSmallModal')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button#closeLargeModal')
