from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config
import tempfile


def apply_stealth(driver):
    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """)

    driver.execute_script("""
        window.navigator.chrome = {
            runtime: {}
        }
    """)

    driver.execute_script("""
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3]
        })
    """)

    driver.execute_script("""
        Object.defineProperty(navigator, 'languages', {
            get: () => ['en-US', 'en']
        })
    """)

    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
            """
        },
    )

def create_driver():
    options = Options()

    # User Agents
    user_agents = config.USER_AGENTS
    usr_agent = user_agents[-1]
    options.add_argument(f"user-agent={usr_agent}")

    # Linux Stability Fixes
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Window size
    options.add_argument("--window-size=1366,768")

    # Isolated profile
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    # Remove "controlled by automated test software"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    apply_stealth(driver=driver)
    return driver
