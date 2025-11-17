from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.locators import Selectors as S
from src.pages.product_page import ProductPage


class CategoryPage(BasePage):
    """Page object for a specific category (product listing) page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def assert_header_is(self, category_name: str) -> None:
        """
        Assert that there is an <h1> on the page that contains the given category name.
        We do NOT require it to be visible, because some themes duplicate headers
        (desktop/mobile, SEO) and hide some of them.
        """
        header = self.page.locator(S.CategoryPage.HEADER_TITLE).filter(
            has_text=category_name
        )

        # Just assert that at least one such <h1> exists in the DOM
        count = header.count()
        assert count > 0, (
            f"Expected at least one <h1> with text '{category_name}', "
            f"but found {count}"
        )

    def assert_products_are_visible(self) -> None:
        """
        Assert that there is at least one visible product on the category page.
        """
        # Each ".product-layout.product-list" is a product card
        products = self.page.locator(S.CategoryPage.PRODUCT_LIST_CONTAINER)

        # Check that we have at least one product in the DOM
        count = products.count()
        assert count > 0, f"Expected at least one product, but found {count}"

        # Check that the first product card is visible
        first_product = products.first
        expect(
            first_product,
            "At least one product card should be visible on the category page",
        ).to_be_visible()

    def open_first_product(self) -> ProductPage:
        """
        Open the first product from the listing and return ProductPage.
        """
        # Click on the first product title/link
        self.page.locator(S.ProductPage.PRODUCT_ITEM_LINK).first.click()
        return ProductPage(self.page)
