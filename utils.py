from playwright.sync_api import Page

# Функция для ожидания - что бы задать время и увидеть что происходит в браузере
def wait(page: Page, timeout_ms: int):
    page.wait_for_timeout(timeout_ms)