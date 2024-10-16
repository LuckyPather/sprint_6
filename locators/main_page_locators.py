from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_UNIVERSAL_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_UNIVERSAL_LOCATOR = By.ID, 'accordion__panel-{}'

    QUESTION_8 = By.ID, 'accordion__heading-7'


