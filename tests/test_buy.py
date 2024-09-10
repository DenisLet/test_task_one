import pytest
from site_selectors.site_selectors import Selectors
from utils import wait

@pytest.mark.parametrize("delay", [2000])  # Параметризируем задержку
def test_purchase(page_context, delay: int):
    page = page_context

    # Авторизация
    page.goto(Selectors.URL)
    wait(page, delay)
    page.fill(Selectors.USERNAME, "standard_user")
    page.fill(Selectors.PASSWORD, "secret_sauce")
    page.click(Selectors.LOGIN_BUTTON)
    wait(page, delay)

    # Выбор товара
    page.click(Selectors.TARGET_NAME)
    page.click(Selectors.ADD_TO_CART)
    wait(page, delay)

    # Переход в корзину
    page.click(Selectors.CART)
    assert page.is_visible(Selectors.TARGET_NAME)
    wait(page, delay)

    # Оформление заказа
    page.click(Selectors.CHECKOUT)
    page.fill(Selectors.FIRST_NAME, "Dr.Dre")
    page.fill(Selectors.LAST_NAME, "Snoop Dog")
    page.fill(Selectors.POSTAL_CODE, "Still D.R.E.")
    wait(page, delay)
    page.click(Selectors.CONTINUE)
    wait(page, delay)

    # Подтверждение заказа
    page.click(Selectors.FINISH)
    wait(page, delay)

    # Проверка успешного завершения покупки
    assert page.is_visible(Selectors.FINAL_MESSAGE)
    wait(page, delay)
