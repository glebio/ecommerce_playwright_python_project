from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.locators import Selectors as S
import re


class SearchResultsPage(BasePage):
    """Page object for the search results page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    # ---------- Locators wrappers ----------
    def _products(self):
        """Return locator for all product items in the search results."""
        return self.page.locator(S.ProductPage.PRODUCT_ITEM)

    # ---------- Basic helpers ----------
    def get_product_count(self) -> int:
        """Return the number of product items in the search results."""
        return self._products().count()

    def expect_at_least_one_product(self) -> None:
        """Assert that at least one product is visible in the results."""
        products = self._products()
        expect(products.first).to_be_visible()
        count = products.count()
        assert count > 0, f"Expected at least one product in search results, got {count}"

    # ---------- Assertions for titles ----------
    def expect_all_titles_contain(self, term: str, case_insensitive: bool = True) -> None:
        """
        Assert that every product title contains the given term.
        (Efficient version: uses one call to get all texts)
        """

        all_titles = self._products().all_inner_texts()

        assert len(all_titles) > 0, "Expected at least one product before checking titles"

        flags = re.IGNORECASE if case_insensitive else 0
        pattern = re.compile(re.escape(term), flags)

        for text in all_titles:
            assert pattern.search(text), (
                f"Expected product title to contain '{term}', got: {text!r}"
            )

    # ---------- Negative / empty results ----------
    def expect_no_results(self) -> None:
        """Assert that no products are shown in the search results."""
        products = self._products()
        count = products.count()
        assert count == 0, f"Expected 0 products, but got {count}"

    def expect_no_results_message(self) -> None:
        """
        Assert that the 'no products found' message is displayed.
        Adjust the text according to your store's theme if needed.
        """
        content_area = self.page.locator("#content")
        expect(content_area).to_contain_text(
            "There is no product that matches the search criteria"
        )

    def expect_compare_total_hidden(self) -> None:
        """
        Assert that the compare-total element is hidden or not visible.
        This is a more theme-specific check.
        """
        compare_total = self.page.locator("#compare-total")
        expect(compare_total).to_be_hidden()

    # ---------- URL helpers (optional) ----------
    def assert_url_contains_search_param(self, expected_part: str = "search=") -> None:
        """
        Assert that the current URL contains the given substring.
        """
        current_url = self.page.url
        assert expected_part in current_url, (
            f"Expected '{expected_part}' to be present in URL '{current_url}'"
        )