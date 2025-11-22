# 🛒 E-Commerce Test Automation Framework (Playwright / Python)

![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/playwright-1.40%2B-brightgreen?logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-8.0%2B-blue?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
---

Made with ❤️ by the professionals at [**QAresults**](https://qaresults.com) — Let’s Make Your Product Better with
Automated Testing!

---

## 📑 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Implemented Test Scenarios](#implemented-test-scenarios)
- [Planned / Extended Test Coverage](#planned--extended-test-coverage)
- [Contributing](#contributing)
- [License](#license)

---

## 🔭 Overview

This **Test Framework** provides robust and maintainable UI test automation for **E-commerce websites**.

For a real demonstration of how the automated tests work, our team developed a dedicated test
website 🚀: <a href="https://shop.qaresults.com" target="_blank">shop.qaresults.com</a>&nbsp;<br/><br/>
[![Shop Screenshot](https://github.com/user-attachments/assets/ad92704b-a6bb-4779-9b33-24cf3326280f "Click to open test store")](https://shop.qaresults.com)<br/><br/>

Framework is built with:
- ![Playwright](https://img.shields.io/badge/-Playwright-45ba63?logo=playwright&logoColor=white) [Playwright](https://playwright.dev/python/)
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) [Python](https://www.python.org/)
- ![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?logo=pytest&logoColor=white) [Pytest](https://docs.pytest.org/)

It focuses on validating critical user flows such as **product search**, **filtering**, **sorting**, **user-generated
interactions** (like reviews and ratings) ond others.

---
## ✨ Key Features

* **Page Object Model (POM):** Strict separation between test logic (what to test) and page interaction (how to test).
* **Fluent Interface:** Page methods return other Page Objects, allowing for readable method chaining (e.g., `home.search("iPhone").open_first_product()`).
* **Smart Locators:** Centralized locator storage (`src/locators.py`) for easy maintenance.
* **Cross-Browser:** Supports Chromium (Chrome), Firefox, and WebKit (Safari).
* **Environment Management:** Configuration via `.env` files and `pytest.ini`.
* **Robust Assertions:** Uses Playwright's auto-retrying assertions to eliminate flaky tests.

---
## Key Features

- **Playwright + Pytest + POM**
    - Clear Page Object Model structure with reusable page classes.
- **Automated UI Tests**
    - Covers key user journeys: search, category navigation, add to cart (guest).
- **Centralized Selectors**
    - All locators stored in a single `Selectors` class to simplify maintenance.
- **Environment Configuration**
    - Base URL and other settings are loaded from `.env`.
- **Scalable Architecture**
    - Ready to extend with more pages, utilities, parametrized tests and CI/CD integration.

## Requirements

- **Python** 3.12+
- **Playwright for Python**
- **Pytest**
- A modern browser (Chromium / Chrome; can be extended to Firefox/WebKit)

All Python dependencies are listed in `requirements.txt`.

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/glebio/ecommerce_playwright_python_project.git
cd ecommerce_playwright_python_project
```
---
## 📂 Project Structure

```text
ecommerce_playwright_python_project/
├── .venv/                        # Python Virtual Environment (Git ignored)
├── data/                         # Test data files (JSON, CSV)
├── reports/                      # Test reports (Allure, HTML)
├── src/                          # Framework Core
│   ├── locators.py               # 📍 Centralized UI Selectors
│   ├── pages/                    # 📄 Page Object Models
│   │   ├── base_page.py          # Common methods for all pages
│   │   ├── home_page.py
│   │   ├── search_results_page.py
│   │   ├── category_page.py
│   │   ├── product_page.py
│   │   └── cart_page.py
│   └── utils/                    # 🛠 Utilities & Config loaders
│       └── config.py
├── tests/                        # 🧪 Test Specifications
│   ├── e2e/                      # End-to-End Tests
│   │   ├── test_search.py
│   │   ├── test_category_navigation.py
│   │   └── test_add_to_cart.py
│   └── conftest.py               # Pytest Fixtures (Browser setup)
├── .env                          # Environment Variables (Git ignored)
├── .gitignore                    # Git ignore rules
├── pytest.ini                    # Pytest configuration & markers
├── requirements.txt              # Python dependencies
└── README.md                     # Project Documentation
```
## Contributing

Contributions are welcome! Please follow our existing coding conventions and testing standards. If you add or revise
tests, remember to update this coverage list (or any separate documentation) to keep everything in sync.

## License

This project is licensed under the **MIT License**.