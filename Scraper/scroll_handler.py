from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from Scraper.data_extractor import map_link_extractor
import random
from config import logger


def get_feed(wait):
    try:
        return wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="feed"]')))
    except TimeoutException as e:
        logger.warning(f"Timeout Exception occurred : {e}")
        return wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"Results")]')))


def human_scroll_panel(driver):
    wait = WebDriverWait(driver, 20)
    no_change_count = 0
    while no_change_count < 7:
        try:
            feed = get_feed(wait)

            # Extract data before scroll
            new_cards = map_link_extractor(driver=driver, feed=feed)

            if new_cards < 1:
                no_change_count += 1
            else:
                no_change_count = 0

            # Set origin
            origin = ScrollOrigin.from_element(feed)

            # Scroll down
            ActionChains(driver).scroll_from_origin(
                origin,
                delta_x=0,
                delta_y=random.randint(500, 900)
            ).perform()

            # Optional small upward scroll
            if random.random() < 0.2:
                origin = ScrollOrigin.from_element(feed)
                ActionChains(driver).scroll_from_origin(
                    origin,
                    delta_x=0,
                    delta_y=-random.randint(100, 200)
                ).perform()

            if driver.find_elements(By.XPATH, '//span[contains(text(),"end")]'):
                logger.info("End of list ------ Stopping Scrolling")
                break

        except StaleElementReferenceException as e:
            logger.warning(f"StaleElementReferenceException occurred : {e}")
            continue

    logger.info("Scrolling complete. Fetching data for each card")