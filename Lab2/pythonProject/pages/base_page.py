from playwright.sync_api import Page, Playwright, sync_playwright, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)