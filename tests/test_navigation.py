"""Tests for the plawright.dev site"""

from pages.MainPage import MainPage


def test_home_page_title(page):
    """Tests the title of the page"""
    main_page = MainPage(page)
    main_page.navigate()
    title = "Fast and reliable end-to-end testing for modern web apps"
    title += " | Playwright"
    assert main_page.title() == title
