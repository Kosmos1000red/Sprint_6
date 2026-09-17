import allure

from data import OrderData, URLs
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий: кнопка «Заказать» вверху страницы")
def test_order_scooter_via_header_button(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()
    main_page.click_order_button_header()

    order_page.fill_first_form(OrderData.ORDER_1)
    order_page.fill_second_form(OrderData.ORDER_1)
    order_page.confirm_order()

    assert order_page.is_success_modal_visible(), \
        "Модальное окно успешного заказа не появилось"


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий: кнопка «Заказать» внизу страницы")
def test_order_scooter_via_footer_button(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()
    main_page.click_order_button_footer()

    order_page.fill_first_form(OrderData.ORDER_2)
    order_page.fill_second_form(OrderData.ORDER_2)
    order_page.confirm_order()

    assert order_page.is_success_modal_visible(), \
        "Модальное окно успешного заказа не появилось"


@allure.feature("Навигация")
@allure.story("Логотип «Самокат» ведёт на главную")
def test_scooter_logo_redirects_to_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_scooter_logo()

    assert main_page.get_current_url() == URLs.BASE_URL


@allure.feature("Навигация")
@allure.story("Логотип «Яндекс» открывает Дзен в новой вкладке")
def test_yandex_logo_redirects_to_dzen(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()

    original_window = main_page.get_current_window()
    main_page.click_yandex_logo()

    new_window = main_page.wait_for_second_window(original_window)
    main_page.switch_to_window(new_window)
    main_page.wait_for_url_contains(URLs.DZEN_DOMAIN)

    assert URLs.DZEN_DOMAIN in main_page.get_current_url()