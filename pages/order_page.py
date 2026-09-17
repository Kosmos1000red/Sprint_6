from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_first_form(self, data):
        self.send_keys(OrderPageLocators.NAME_INPUT, data["name"])
        self.send_keys(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.METRO_OPTION(data["metro"]))
        self.send_keys(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, data):
        self.send_keys(OrderPageLocators.DATE_INPUT, data["date"])
        self.press_enter(OrderPageLocators.DATE_INPUT)

        self.scroll_to(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.RENTAL_PERIOD_OPTION(data["rental_period"])
            )
        )
        self.click(OrderPageLocators.RENTAL_PERIOD_OPTION(data["rental_period"]))

        self.scroll_to(OrderPageLocators.COLOR_CHECKBOX(data["color"]))
        self.click(OrderPageLocators.COLOR_CHECKBOX(data["color"]))

        self.send_keys(OrderPageLocators.COMMENT_INPUT, data["comment"])

    def confirm_order(self):
        self.click_with_scroll(OrderPageLocators.ORDER_BUTTON)
        self.wait_until_visible(OrderPageLocators.CONFIRM_MODAL)
        self.click_with_scroll(OrderPageLocators.CONFIRM_BUTTON)

    def is_success_modal_visible(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MODAL)