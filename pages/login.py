from pages.base_page import BasePage
from config.config import USERNAME, PASSWORD

class LoginPage(BasePage):
    def sign_in(self, username=None, password=None):
        username = username or USERNAME
        password = password or PASSWORD

        if username is None or password is None:
            raise ValueError("USERNAME and PASSWORD must be provided either as arguments or in the environment")

        self.page.get_by_role("link", name="Sign In").click()
        self.submit_credentials(username, password)

    def submit_credentials(self, username, password):
        self.page.get_by_placeholder("Email").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
