import pytest
import allure

from pages.main_page import MainPage


@allure.feature("FAQ")
@allure.story("Выпадающий список «Вопросы о важном»")
@pytest.mark.parametrize(
    "index, expected_fragment",
    [
        (1, "Сутки — 400 рублей"),
        (2, "Пока что у нас так"),
        (3, "Допустим, вы оформляете заказ"),
        (4, "Только начиная с завтрашнего дня"),
        (5, "Пока что нет"),
        (6, "Самокат приезжает к вам с полной зарядкой"),
        (7, "Да, пока самокат не привезли"),
        (8, "Да, обязательно"),
    ],
)
def test_faq(driver, index, expected_fragment):
    main_page = MainPage(driver)
    main_page.open_main_page()
    main_page.click_faq_question(index)
    answer = main_page.get_faq_answer_text(index)
    assert expected_fragment in answer, (
        f"Ответ на вопрос {index} не содержит '{expected_fragment}'. "
        f"Фактический текст: {answer!r}"
    )