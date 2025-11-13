import pytest
from playwright.sync_api import Page

from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.smoke
def test_search_for_existing_product(page: Page):
    """
    Test Case: Search for an existing product (Happy Path).
    Steps:
    1. Navigate to the homepage.
    2. Enter a valid product name in the search bar.
    3. Click the search button.
    4. Verify that results are displayed and look relevant.
    """
    home = HomePage(page)
    search_query = "MacBook"  # TODO: replace with a product that definitely exists

    home.open()
    results_page: SearchResultsPage = home.search(search_query)
    results_page.assert_has_results()
    results_page.assert_first_result_contains(search_query)
    results_page.assert_url_contains_search_param("search=")


def test_search_no_results(page: Page):
    """
    Test Case: Search for a non-existing product (Negative Path).
    Steps:
    1. Navigate to the homepage.
    2. Enter a nonsense string.
    3. Click the search button.
    4. Verify that a 'no products found' message is displayed.
    """
    home = HomePage(page)
    nonsense_query = "non_existing_item"

    home.open()
    results_page: SearchResultsPage = home.search(nonsense_query)
    results_page.assert_no_results_message_is_shown()