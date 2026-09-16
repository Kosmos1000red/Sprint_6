from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    def open_main_page(self):
        self.open(self.URL)

    def click_order_button_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_footer(self):
        self.click(MainPageLocators.ORDER_BUTTON_FOOTER)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def click_faq_question(self, index):
        element = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.FAQ_QUESTION(index))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element.click()

    def get_faq_answer_text(self, index):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.FAQ_ANSWER(index))
        )
        return self.get_text(MainPageLocators.FAQ_ANSWER(index))