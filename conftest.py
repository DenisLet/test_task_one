import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def playwright() -> Playwright:
    # Запуск Playwright (синхронно)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        yield p
