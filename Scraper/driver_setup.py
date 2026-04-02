import config
import undetected_chromedriver as uc
import os
import subprocess


def create_driver():

    options = uc.ChromeOptions()
    # User Agents
    user_agents = config.USER_AGENTS
    usr_agent = user_agents[-1]
    options.add_argument(f"user-agent={usr_agent}")

    if config.HEADLESS:
        options.add_argument("--headless=new")

    # Linux Stability Fixes
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Window size
    options.add_argument("--window-size=1366,768")
    # Profile directory for storage of the browser data
    base_dir = config.PROJECT_ROOT
    profile_path = os.path.join(base_dir, "chrome_profile")
    options.add_argument(
        f"--user-data-dir={profile_path}"
    )
    # Patched Selenium WebDriver
    version = subprocess.check_output(
        ["google-chrome", "--version"]
    ).decode().split()[2].split(".")[0]
    driver = uc.Chrome(version_main=int(version), options=options)

    return driver