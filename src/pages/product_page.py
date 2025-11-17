from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.locators import Selectors as S
from src.pages.cart_page import CartPage


class ProductPage(BasePage):
    """Page object for the product details (PDP) page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_product_name(self) -> str:
        """Return the product title text from the PDP."""
        title = self.page.locator(S.ProductPage.PRODUCT_TITLE)
        expect(title, "Product title should be visible on PDP").to_be_visible()
        return title.inner_text().strip()

    def add_to_cart(self) -> None:
        """Click on the 'Add to Cart' button."""
        self.page.locator(S.ProductPage.ADD_TO_CART_BUTTON).click()

    def open_cart_dropdown(self) -> None:
        """
        Open the cart dropdown (mini-cart) from the header.
        """
        self.page.locator(S.ProductPage.CART_BUTTON).click()

    def go_to_cart_page(self) -> CartPage:
        """
        Open the full cart page via the cart dropdown.
        """
        self.open_cart_dropdown()
        self.page.locator(S.ProductPage.VIEW_CART_BUTTON).click()
        return CartPage(self.page)