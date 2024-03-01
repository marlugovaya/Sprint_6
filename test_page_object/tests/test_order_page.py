import pytest
import datetime


class TestOrderPage:
    @pytest.mark.parametrize("is_header_button, name, surname, address, metro, phone, delivery_date, rent_period",
                             [(True, 'Котик', 'Котейкин', 'ул. Котиков, д. 5', 'Лубянка', '89123456789',
                              datetime.date.today().day, 'сутки'),
                              (False, 'Собачка', 'Собачкина', 'ул. Собачек, д. 8', 'ВДНХ', '89876543212',
                              datetime.date.today().day, 'трое суток')]
                             )
    def test_scooter_order_true(self, main_page, order_page, is_header_button, name, surname,
                                address, metro, phone, delivery_date, rent_period):
        main_page.click_order_button(is_header_button)
        order_page.for_who_form(name, surname, address, metro, phone)
        order_page.about_rent_form(delivery_date, rent_period)
        assert 'Заказ оформлен' in order_page.check_order()
