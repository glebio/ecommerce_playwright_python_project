from playwright.sync_api import Page
from src.pages.base_page import BasePage
from src.pages.search_results_page import SearchResultsPage
from src.pages.category_page import CategoryPage
from src.locators import Selectors as S


class HomePage(BasePage):
    """Page object for the home page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open(self) -> None:
        """
        Open the home page using the configured BASE_URL.
        """
        self.goto("/")

    def search(self, text: str) -> SearchResultsPage:
        """
        Perform a search using the search box and return SearchResultsPage.
        """
        # Type into search input
        self.page.fill(S.HomePage.SEARCH_BOX, text)
        # Click search button
        self.page.click(S.HomePage.SEARCH_BUTTON)
        # Return page object for search results
        return SearchResultsPage(self.page)

    def open_categories_menu(self) -> None:
        """
        Open the vertical categories menu if it is collapsed behind a button.
        If there is no such button, this method silently does nothing.
        """
        button = self.page.locator(S.HomePage.BROWSE_CATEGORIES_BUTTON)
        if button.count() > 0:
            button.click()

    def navigate_to_category(self, category_name: str) -> CategoryPage:
        """
        Navigate to a category from the home page vertical menu and return CategoryPage.
        """
        self.open_categories_menu()
        category_selector = S.HomePage.category_link_by_text(category_name)
        # Click on the first matching category link (top-level item)
        self.page.locator(category_selector).first.click()
        return CategoryPage(self.page)

