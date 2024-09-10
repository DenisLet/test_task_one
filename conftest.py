import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def page_context(playwright) -> Page:
    # Выбираем для теста браузер Chromium и делаем его видимым
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()