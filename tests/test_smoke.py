import re

from playwright.sync_api import Page, expect

from pages.home_page import HomePage


def test_home_page_loads(page: Page):
    home = HomePage(page)
    home.open()
    expect(page).to_have_title("Automation Exercise")

def test_navigate_to_login(page: Page):
    home = HomePage(page)
    home.open()
    home.go_to_login()
    expect(page).to_have_url(re.compile("/login"))