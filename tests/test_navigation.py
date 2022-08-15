"""Tests for the plawright.dev site"""
from pages.DocsPage import DocsPage
from pages.MainPage import MainPage


def test_home_page_title(page):
    """Tests the title of the page"""
    main_page = MainPage(page)
    main_page.navigate()
    title = "Fast and reliable end-to-end testing for modern web apps"
    title += " | Playwright"
    assert main_page.title() == title


def test_button_get_started(page):
    """Tests the navigation of the button 'Get Started'"""
    main_page = MainPage(page)
    main_page.navigate()
    main_page.check_am_i_there()
    main_page.button_get_started.click()

    docs_page = DocsPage(page)
    docs_page.check_am_i_there()
    assert docs_page.title() == "Installation | Playwright"
