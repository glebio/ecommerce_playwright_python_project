from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.locators import Selectors as S


class SearchResultsPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def products(self):
        return self.page.locator(S.ProductPage.PRODUCT_ITEM)

    def assert_has_results(self) -> None:
        results = self.products()
        expect(results.first).to_be_visible()
        assert results.count() > 0

    def assert_first_result_contains(self, text: str) -> None:
        first_product_name = self.products().first
        expect(first_product_name).to_contain_text(text, ignore_case=True)

    def assert_no_results_message_is_shown(self) -> None:
        content_area = self.page.locator("#content")
        expect(content_area).to_contain_text(
            "There is no product that matches the search criteria"
        )

    def assert_url_contains_search_param(self, expected_part: str = "search=") -> None:
        expect(self.page).to_have_url(lambda url: expected_part in url)