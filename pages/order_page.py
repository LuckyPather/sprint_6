# Todo: тут я должен создать метод, который принимает тип кнопки заказать, заполняет ордер потом в тесте я проверяю сообщение
import allure

from base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Выбираю тип кнопки заказа")
    def choose_button(self, locator):
        self.scroll_to_element(locator)
        self.click_to_element(locator)

    @allure.step("Заполняю форму заказа")
