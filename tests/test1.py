"""Tests for the plawright.dev site"""

from pages import MainPage


def test_home_page_title(page):
    """Tests the title of the page"""
    main_page = MainPage(page)
    main_page.navigate()
    assert main_page.title() == ""
