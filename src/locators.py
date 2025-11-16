from __future__ import annotations


class Selectors:
    class HomePage:
        SEARCH_BOX = '#text-search'
        SEARCH_BUTTON = '#sp-btn-search'
        ACCOUNT_BUTTON = 'a.dropdown-toggle[title="My Account"]'
        REGISTER_BUTTON = '#pt-register-link'
        LOGIN_BUTTON = '#pt-login-link'
        LOGOUT_BUTTON = '#pt-logout-link'

        BROWSE_CATEGORIES_BUTTON = 'div[class="oc-menu-bar"]'

        MENU_CONTAINER = 'div.vertical-menu .ul-top-items'
        MENU_ITEMS = 'div.vertical-menu .ul-top-items li.li-top-item'
        MENU_LINKS = 'div.vertical-menu .ul-top-items li.li-top-item a'

        @staticmethod
        def category_link_by_text(category_name: str) -> str:
            """
            Locator for a top-level category in the vertical menu by visible text.
            We target only links with class 'a-top-link' to avoid subcategories.
            """
            return (
                f'div.vertical-menu .ul-top-items '
                f'li.li-top-item a.a-top-link:has-text("{category_name}")'
            )

    class ProductPage:
        PRODUCT_ITEM = ".product-item h4"

    class CategoryPage:
        """
        Locators for a product listing category page.
        """

    HEADER_TITLE = "h1"
    PRODUCT_LIST_CONTAINER = ".product-list"
