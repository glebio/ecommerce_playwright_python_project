from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.locators import Selectors as S


class CategoryPage(BasePage):
    """Page object for a specific category (product listing) page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def assert_header_is(self, category_name: str) -> None:
        """
        Assert that the main <h1> header equals the expected category name.
        """
        header = self.page.locator(S.CategoryPage.HEADER_TITLE)
        expect(header, "Category header should be visible").to_be_visible()
        expect(header, "Category header text should match category name").to_have_text(
            category_name
        )

    def assert_products_are_visible(self) -> None:
        """
        Assert that the product list is visible and has at least one product.
        """
        product_list = self.page.locator(S.CategoryPage.PRODUCT_LIST_CONTAINER)
        expect(product_list, "Product list container should be visible").to_be_visible()

        products = product_list.locator(S.ProductPage.PRODUCT_ITEM)
        expect(
            products.first, "At least one product should be visible in the category"
        ).to_be_visible()
