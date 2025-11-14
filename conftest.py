import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):

    return {
        **browser_type_launch_args,
        "channel": "chrome",
        "headless": False,

        "args": [
            "--start-maximized",
            "--window-size=1920,1080",
        ],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):

    return {
        **browser_context_args,
        # Here we can either set explicit viewport size:
        "viewport": {"width": 1920, "height": 1080},
        # or use None to let Playwright use full window size:
        # "viewport": None,
    }