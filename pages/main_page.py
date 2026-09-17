from selenium.webdriver.support import expected_conditions as EC

from data import BASE_URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = BASE_URL

    def open_main_page(self):
        self.open(self.URL)
        self._close_cookie_banner_if_present()

    def _close_cookie_banner_if_present(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    def click_order_button_header(self):
        self.click_with_scroll(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_order_button_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_with_scroll(MainPageLocators.ORDER_BUTTON_FOOTER)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def click_faq_question(self, index):
        self.click_with_scroll(MainPageLocators.FAQ_QUESTION(index))

    def get_faq_answer_text(self, index):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.FAQ_ANSWER(index))
        )
        return self.get_text(MainPageLocators.FAQ_ANSWER(index))