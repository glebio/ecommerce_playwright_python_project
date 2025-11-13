from playwright.sync_api import Page
from src.utils.config import BASE_URL


class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, path: str = "/") -> None:

        if path.startswith("http://") or path.startswith("https://"):
            url = path
        else:
            url = BASE_URL.rstrip("/") + "/" + path.lstrip("/")

        self.page.goto(url)