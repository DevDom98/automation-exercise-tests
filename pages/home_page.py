from playwright.sync_api import Page


class HomePage(Page):
    def __init__(self, page:Page):
        self.page = page
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")

    def open(self):
        self.page.goto("/")

    def go_to_login(self):
        self.signup_login_link.click()