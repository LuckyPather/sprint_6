import allure

from base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Получаю текст вопроса и текст ответа")
    def get_answer_and_question_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_UNIVERSAL_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_UNIVERSAL_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        self.click_to_element(locator_q_formatted)
        question_text = self.get_text_from_element(locator_q_formatted)
        answer_text = self.get_text_from_element(locator_a_formatted)
        return question_text, answer_text
