from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import config
from utils.deduplicator import add_existing_link
from utils.delays import micro_delay
from utils.runtime_json_data import append_to_jsonl
from config import logger


def map_link_extractor(driver, feed):
    wait = WebDriverWait(driver, 20)
    index = 0
    data_results = feed.find_elements(By.XPATH, './/div[@role="article"]')
    new_count = 0
    while True:

        if index >= len(data_results):
            break

        data = data_results[index]

        try:
            name = data.find_element(By.XPATH,
                                     './/div[contains(@class, "fontHeadlineSmall")]'
            ).text
        except NoSuchElementException:
            name = "NA"
        try:
            u_id = data.find_element(By.XPATH, './/a[contains(@href, "/maps/place")]').get_attribute('href')
        except NoSuchElementException:
            u_id = "NA"
        try:
            rating_element = data.find_element(By.XPATH,
            './/span[@role="img"]'
            )
            rating = rating_element.get_attribute('aria-label')
        except NoSuchElementException:
            rating = "NA"

        if not add_existing_link(u_id, name, rating):
            new_count += 1

        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="feed"]')))
        except TimeoutException as e:
            logger.warning(f"Timed out while trying to fetch Feed: {e}")
            pass
        index += 1
    return new_count

def extract_link_data(driver, link):
    wait = WebDriverWait(driver, 20)

    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//h1')))
        try:
            phone = driver.find_element(
                By.XPATH, '//button[contains(@data-tooltip,"phone")]'
            ).text
        except:
            phone = "NA"
        try:
            website = driver.find_element(
                By.XPATH, '//a[@data-item-id="authority"]'
            ).get_attribute("href")
        except:
            website = "NA"
        return phone, website
    except:
        logger.warning(f"Failed to extract phone/website from link: {link}")
        return None, None

def open_link_tabs(driver, links, batch_size = 5):
    seen_places = config.seen_places
    for i in range(0, len(links), batch_size):
        batch_links = links[i:i + batch_size]
        new_tabs = []

        # Open new tabs
        for link in batch_links:
            driver.execute_script(f"window.open('{link}', '_blank');", link)
            micro_delay()
            new_tabs.append(driver.window_handles[-1])

        for link, tab in zip(batch_links, new_tabs):
            try:
                driver.switch_to.window(tab)
                micro_delay()

                # Retry logic
                phone, website = None, None
                for attempt in range(3):
                    phone, website = extract_link_data(driver, link)
                    if phone or website:
                        break
                data = {}
                if phone and phone != "NA":
                    data["phone"] = phone
                if website and website != "NA":
                    data["website"] = website

                if link not in seen_places:
                    seen_places[link] = {}

                if data:
                    seen_places[link].update(data)
                    seen_places[link]["details_fetched"] = True
            except Exception as e:
                logger.warning(f"Error processing {link}. An error occurred : {e}")

        # Save to json
        for link in batch_links:
            record = {link: seen_places[link]}
            append_to_jsonl(record)

        # Close the processed tabs
        for tab in new_tabs:
            driver.switch_to.window(tab)
            driver.close()
            micro_delay()

        # Switch back to main tab
        driver.switch_to.window(driver.window_handles[0])
