from selenium.webdriver.common.by import By
from utils.delays import micro_delay


def map_data_extractor(driver, feed):
    data_results = feed.find_elements(By.XPATH, './/div[@role="article"]')
    for data in data_results:
        try:
            name = data.find_element(By.XPATH,
                                     './/div[contains(@class, "fontHeadlineSmall")]'
            ).text
        except:
            name = "NA"
        try:
            rating_element = data.find_element(By.XPATH,
            './/span[@role="img"]'
            )
            rating = rating_element.get_attribute('aria-label')
        except:
            rating = "NA"
        print(name, rating)
        micro_delay()
