import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def dismiss_consent(page:Page):
    page.add_locator_handler(
        page.get_by_role("button", name="Consent"),
        lambda button: button.click(),
    )