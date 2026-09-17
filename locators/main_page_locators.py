from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[text()='Хорошо']")

    ORDER_BUTTON_HEADER = (
        By.XPATH,
        "//button[text()='Заказать' and ancestor::div[contains(@class,'Header_Nav')]]"
    )
    ORDER_BUTTON_FOOTER = (
        By.XPATH,
        "//button[text()='Заказать' and ancestor::div[contains(@class,'Home_FinishButton')]]"
    )

    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    FAQ_QUESTION = lambda index: (By.ID, f"accordion__heading-{index - 1}")
    FAQ_ANSWER = lambda index: (By.ID, f"accordion__panel-{index - 1}")