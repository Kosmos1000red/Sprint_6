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
        self.find(OrderPageLocators.DATE_INPUT).send_keys("\ue007")

        dropdown = self.find(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", dropdown
        )
        self.driver.execute_script("arguments[0].click();", dropdown)

        option = self.wait.until(
            EC.visibility_of_element_located(
                OrderPageLocators.RENTAL_PERIOD_OPTION(data["rental_period"])
            )
        )
        self.driver.execute_script("arguments[0].click();", option)

        checkbox = self.find(OrderPageLocators.COLOR_CHECKBOX(data["color"]))
        self.driver.execute_script("arguments[0].click();", checkbox)

        self.send_keys(OrderPageLocators.COMMENT_INPUT, data["comment"])

    def confirm_order(self):
        order_btn = self.find(OrderPageLocators.ORDER_BUTTON)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", order_btn
        )
        self.driver.execute_script("arguments[0].click();", order_btn)

        self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.CONFIRM_MODAL)
        )

        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", confirm_btn)

    def is_success_modal_visible(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MODAL)