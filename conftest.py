#This is a buffer file for pytest fixtures. You can add your own fixtures here to be used across multiple test files.

# from playwright.sync_api import sync_playwright
# import pytest


# @pytest.fixture(scope="module")
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     page.close()