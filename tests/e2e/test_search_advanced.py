import pytest
from playwright.sync_api import Page

from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.smoke
def test_search_exact_match_only_relevant_products(page: Page):
    """
    Search for a specific product name (e.g. 'iPhone') and verify that:
    - at least one product is returned
    - each product title contains the search term
    - URL contains search query parameter
    """
    home = HomePage(page)
    search_query = "iPhone"

    # Arrange
    home.open()

    # Act
    results_page: SearchResultsPage = home.search(search_query)

    # Assert
    results_page.expect_at_least_one_product()
    results_page.expect_all_titles_contain(search_query)
    results_page.assert_url_contains_search_param("search=")


@pytest.mark.smoke
def test_search_partial_match_results(page: Page):
    """
    Search using a partial term (e.g. 'Phone') and verify that:
    - at least one result is returned
    - each product title contains the partial term
    - URL contains search query parameter
    """
    home = HomePage(page)
    search_query = "Phone"

    # Arrange
    home.open()

    # Act
    results_page: SearchResultsPage = home.search(search_query)

    # Assert
    results_page.expect_at_least_one_product()
    results_page.expect_all_titles_contain(search_query)
    results_page.assert_url_contains_search_param("search=")


def test_search_no_results_shows_empty_state(page: Page):
    """
    Search for a non-existing product and verify:
    - no products are shown
    - 'no results' message is displayed
    - optionally: compare-total element is hidden
    """
    home = HomePage(page)
    search_query = "NonExistingProduct_12345"

    # Arrange
    home.open()

    # Act
    results_page: SearchResultsPage = home.search(search_query)

    # Assert: no products at all
    results_page.expect_no_results()

    # Assert: empty-state message is visible
    results_page.expect_no_results_message()