import time

from pages.order_page import OrderPage
from locators.order_page_locators import OrderCard, ButtonChoose
from data import Url
from helpers import Generator
import allure
import pytest


class TestOrderPage:
    @allure.title("Оформление заказа")
    @allure.description("Проверяю оформление заказа, используя несколько точек входа на страницу формирования заказа")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('button_order', [
        ButtonChoose.DOWN_BUTTON_GET_ORDER
    ])
    def test_create_order(self, connection, button_order):
        order_page = OrderPage(connection)
        generator = Generator()

        connection.get(Url.MAIN_PAGE_URL)
        time.sleep(3)
        order_page.choose_button(button_order)
        order_page.create_order(generator.name, generator.surname, generator.address, generator.metro_station,
                                generator.phone_number, generator.data, generator.option_term,
                                generator.colors, generator.comment)

        assert "Заказ оформлен" in order_page.get_text_from_element(OrderCard.SUCCESS_MESSAGE), "Проверка не прошла"
