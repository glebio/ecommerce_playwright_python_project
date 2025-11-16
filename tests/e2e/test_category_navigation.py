import pytest
from playwright.sync_api import Page

from src.pages.home_page import HomePage
from src.pages.category_page import CategoryPage


@pytest.mark.smoke
def test_navigate_to_category_and_see_products(page: Page):
    """
    Smoke test:
    Navigate to a category from the home page and verify that products are shown.

    Steps:
    1. Open home page.
    2. Open vertical categories menu (if needed).
    3. Click on a specific category in the menu.
    4. Verify that the category header is correct.
    5. Verify that the category page displays at least one product.
    """
    home = HomePage(page)

    # TODO: choose a category that definitely exists in your store
    category_to_test = "Smartphones & Accessories"

    # 1. Open home page
    home.open()

    # 2–3. Navigate to the category via POM
    category_page: CategoryPage = home.navigate_to_category(category_to_test)

    # 4. Check header text
    category_page.assert_header_is(category_to_test)

    # 5. Check products are visible in the listing
    category_page.assert_products_are_visible()