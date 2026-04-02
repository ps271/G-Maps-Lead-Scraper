from utils.delays import human_delay
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from Scraper.data_extractor import map_data_extractor
import random


def human_scroll_panel(driver):
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 20)
    for _ in range(random.randint(8, 10)):
        # Wait for results panel
        try:
            feed = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="feed"]')))
        except:
            feed = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"Results")]')))
        # Extract Map Data
        map_data_extractor(driver=driver, feed=feed)
        # Move mouse to feed
        origin = ScrollOrigin.from_element(feed)
        # Move mouse over feed
        actions.move_to_element(feed).perform()
        # Scroll down sidebar
        for _ in range(random.randint(2, 4)):
            actions.scroll_from_origin(scroll_origin=origin,
                                       delta_x=0,
                                       delta_y=random.randint(300, 500)
            ).perform()
            human_delay(0.5, 2)

        human_delay(1, 3)