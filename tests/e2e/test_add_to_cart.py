import pytest
from playwright.sync_api import Page
from src.pages.home_page import HomePage
from src.pages.category_page import CategoryPage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage


@pytest.mark.smoke
def test_add_first_product_to_cart_from_category(page: Page):
    """
    Smoke test:
    Add the first product from a category to the cart (guest user).

    Steps:
    1. Open home page.
    2. Navigate to a specific category.
    3. Open the first product from the listing.
    4. Add the product to the cart.
    5. Open the full cart page.
    6. Verify that the product appears in the cart.
    """
    home = HomePage(page)
    category_to_test = "Smartphones & Accessories"  # stable category

    # 1. Open home page
    home.open()

    # 2. Navigate to category
    category_page: CategoryPage = home.navigate_to_category(category_to_test)
    category_page.assert_products_are_visible()

    # 3. Open first product from listing
    product_page: ProductPage = category_page.open_first_product()
    product_name = product_page.get_product_name()

    # 4. Add product to cart
    product_page.add_to_cart()

    # 5. Go to full cart page
    cart_page: CartPage = product_page.go_to_cart_page()

    # 6. Verify product is present in cart
    cart_page.assert_product_in_cart(product_name)