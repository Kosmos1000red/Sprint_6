from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_with_scroll(self, locator):
        self.scroll_to(locator)
        self.js_click(locator)

    def press_enter(self, locator):
        self.find(locator).send_keys("\ue007")

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window(self):
        return self.driver.current_window_handle

    def wait_for_second_window(self, original_window):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        windows = set(self.driver.window_handles) - {original_window}
        return windows.pop()

    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    def wait_for_url_contains(self, fragment):
        self.wait.until(lambda d: fragment in d.current_url)