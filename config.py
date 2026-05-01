import os
from dotenv import load_dotenv
from utils.config_utils import get_env, get_bool, get_int, get_list
import logging


# Project root = same directory as config.py
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

# Configure logging
logging.basicConfig(
    filename=f'{PROJECT_ROOT}/logs/scraper.log',       # file where logs are saved
    level=logging.INFO,           # log INFO and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

logger = logging.getLogger(__name__)

# Single Values
KEYWORD = get_env("KEYWORD")
LOCATION = get_env("LOCATION")

# Boolean / Integer
HEADLESS = get_bool("HEADLESS", False)
MAX_LEADS = get_int("MAX_LEADS", 500)

# Multiple Values
KEYWORDS = get_list("KEYWORDS")
LOCATIONS = get_list("LOCATIONS")

USER_AGENTS = [
    # Chrome Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/121.0.0.0 Safari/537.36",

    # Chrome Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36",

    # Firefox Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) "
    "Gecko/20100101 Firefox/122.0",

    # Firefox Linux
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) "
    "Gecko/20100101 Firefox/121.0",

    # Safari Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "Version/16.4 Safari/605.1.15",

    # Linux
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/145.0.0.0 Safari/537.36"
]

seen_places = {}
