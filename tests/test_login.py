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


def test_login_invalid_credentials_show_error(page: Page):
    """Reject credentials that do not belong to an account."""
    login_page = LoginPage(page)
    login_page.navigate("auth")
    login_page.submit_credentials("nobody@example.invalid", "invalid-test-password")

    expect(page.get_by_text("Invalid login credentials", exact=True)).to_be_visible()
    expect(page).to_have_url("https://foodsavers.app/auth")


def test_login_requires_email(page: Page):
    """Require an email address before submitting the login form."""
    login_page = LoginPage(page)
    login_page.navigate("auth")
    password = page.get_by_placeholder("Password")
    email = page.get_by_placeholder("Email")
    password.fill("invalid-test-password")
    page.get_by_role("button", name="Login").click()

    assert email.evaluate("(element) => element.validity.valueMissing")
    expect(page).to_have_url("https://foodsavers.app/auth")


def test_login_requires_password(page: Page):
    """Require a password before submitting the login form."""
    login_page = LoginPage(page)
    login_page.navigate("auth")
    email = page.get_by_placeholder("Email")
    password = page.get_by_placeholder("Password")
    email.fill("nobody@example.invalid")
    page.get_by_role("button", name="Login").click()

    assert password.evaluate("(element) => element.validity.valueMissing")
    expect(page).to_have_url("https://foodsavers.app/auth")


def test_login_rejects_malformed_email(page: Page):
    """Reject malformed email addresses in the browser before submission."""
    login_page = LoginPage(page)
    login_page.navigate("auth")
    email = page.get_by_placeholder("Email")
    email.fill("not-an-email")
    page.get_by_placeholder("Password").fill("invalid-test-password")
    page.get_by_role("button", name="Login").click()

    assert email.evaluate("(element) => element.validity.typeMismatch")
    expect(page).to_have_url("https://foodsavers.app/auth")
