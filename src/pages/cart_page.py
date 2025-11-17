from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.locators import Selectors as S


class CartPage(BasePage):
    """Page object for the shopping cart page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def assert_product_in_cart(self, product_name: str) -> None:
        """
        Assert that a product with the given name is present in the cart table.
        """
        rows = self.page.locator(S.CartPage.CART_ITEM)
        expect(
            rows.first, "Cart should contain at least one row with product data"
        ).to_be_visible()

        # Look for a row that contains the product name text
        matching_row = rows.filter(has_text=product_name)
        count = matching_row.count()
        assert count > 0, (
            f"Expected product '{product_name}' to be present in cart, "
            f"but did not find it."
        )

    def assert_items_count_at_least(self, min_count: int = 1) -> None:
        """
        Optional: Assert cart has at least `min_count` items (by rows).
        """
        rows = self.page.locator(S.CartPage.CART_ITEM)
        count = rows.count()
        assert count >= min_count, (
            f"Expected at least {min_count} item(s) in cart, but found {count}"
        )