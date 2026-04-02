from Scraper.driver_setup import create_driver
from Scraper.scroll_handler import human_scroll_panel
import config


def main():

    driver = create_driver()

    keyword = config.KEYWORD
    location = config.LOCATION

    search_query = f"{keyword} in {location}"

    url = f"https://www.google.com/maps/search/{search_query}"

    driver.get(url)
    human_scroll_panel(driver)

    input("Press ENTER to close...")

    driver.quit()


if __name__ == "__main__":
    main()