from Scraper.driver_setup import create_driver
from Scraper.scroll_handler import human_scroll_panel
from Scraper.data_extractor import open_link_tabs
import config
from utils.excel import create_excel
from utils.runtime_json_data import load_from_jsonl


def main():

    driver = create_driver()

    keyword = config.KEYWORD
    location = config.LOCATION
    logger = config.logger

    search_query = f"{keyword} in {location}"

    url = f"https://www.google.com/maps/search/{search_query}"

    driver.get(url)
    human_scroll_panel(driver)
    seen_places = config.seen_places
    links = list(seen_places.keys())
    logger.info(f"Found {len(links)} links")
    open_link_tabs(driver, links)

    # File writing
    data = load_from_jsonl()
    create_excel(data)

    input("Press ENTER to close...")

    driver.quit()


if __name__ == "__main__":
    main()
