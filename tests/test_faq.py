import pytest
import allure

from data import FAQ_DATA
from pages.main_page import MainPage


@allure.feature("FAQ")
@allure.story("Выпадающий список «Вопросы о важном»")
@pytest.mark.parametrize("index, expected_text", FAQ_DATA)
def test_faq(driver, index, expected_text):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_faq_question(index)

    actual_text = main_page.get_faq_answer_text(index)

    assert actual_text == expected_text, (
        f"Ответ на вопрос {index} не совпадает.\n"
        f"Ожидалось: {expected_text!r}\n"
        f"Фактически: {actual_text!r}"
    )