from playwright.sync_api import Page
from config.config import BASE_URL

class BasePage:
    base_url = BASE_URL

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path=""):
        self.page.goto(self.base_url + path)
