from src.pages.base_page import BasePage
from src.locators import Selectors as S
from src.pages.search_results_page import SearchResultsPage


class HomePage(BasePage):
    """Page object for the home page."""

    def open(self) -> None:

        self.goto("/")

    def search(self, query: str) -> SearchResultsPage:

        self.page.locator(S.HomePage.SEARCH_BOX).fill(query)
        self.page.locator(S.HomePage.SEARCH_BUTTON).click()
        return SearchResultsPage(self.page)