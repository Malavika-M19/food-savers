from playwright.sync_api import Page, expect
from pages.login import LoginPage
#from config.config import USERNAME, PASSWORD

#_______________________Test Cases_______________________#

def test_login_valid_credentials(page: Page):
    """Verify login with valid email/password"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.sign_in()
    expect(page).to_have_url("https://foodsavers.app/splash")