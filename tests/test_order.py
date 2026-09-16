import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA_1, ORDER_DATA_2


@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий")
@pytest.mark.parametrize(
    "entry_point, order_data",
    [
        ("header", ORDER_DATA_1),
        ("footer", ORDER_DATA_2),
    ],
)
def test_order_scooter(driver, entry_point, order_data):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()

    if entry_point == "header":
        main_page.click_order_button_header()
    else:
        main_page.click_order_button_footer()

    order_page.fill_first_form(order_data)
    order_page.fill_second_form(order_data)
    order_page.confirm_order()

    assert order_page.is_success_modal_visible(), \
        "Модальное окно успешного заказа не появилось"


@allure.feature("Навигация")
@allure.story("Логотип Самокат")
def test_scooter_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_scooter_logo()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


@allure.feature("Навигация")
@allure.story("Логотип Яндекс")
def test_yandex_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()

    original_window = driver.current_window_handle
    main_page.click_yandex_logo()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            break

    WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url)

    assert "dzen.ru" in driver.current_url