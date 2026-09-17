from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = lambda station: (By.XPATH, f"//div[text()='{station}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    RENTAL_PERIOD_DROPDOWN = (
        By.XPATH, "//div[contains(@class,'Dropdown-control')]"
    )
    RENTAL_PERIOD_OPTION = lambda period: (
        By.XPATH,
        f"//div[contains(@class,'Dropdown-option') and text()='{period}']"
    )

    COLOR_CHECKBOX = lambda color: (By.XPATH, f"//label[text()='{color}']/input")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Заказать' and ancestor::div[contains(@class,'Order_Content')]]"
    )

    CONFIRM_MODAL = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'Order_Modal')]//button[text()='Да']"
    )
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")