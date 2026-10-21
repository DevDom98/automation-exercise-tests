from playwright.sync_api import Page, expect


def test_home_page_loads(page: Page):
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")