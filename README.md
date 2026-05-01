# G-Maps-Lead-Scraper

A **configurable Python-based Google Maps scraping system** designed to extract card listings based on search keyword
and location.
This project implements a structured approach with web-driver creation, scrolling through feed, deduplication logic, 
valuable data extraction and secure credential management.

---

## Features

- **Keyword search for a particular location**
- **Logging:** Tracks scraping activity, warnings, and errors in `scraper.log`.
- **Duplicate Prevention:** Keeps track of previously scraped card links to avoid duplicates.
- **Json and Excel Output:** Structured output for easy data consumption and further analysis.
- **Lightweight & Configurable:** Only requires `selenium`, `pandas`, `openpyxl`, `python-dotenv` and `webdriver-manager`
- **Environment Variable Support**(.env)
- **Config Driven Architecture**

---

## Tech Stack

- Python 3.x
- Selenium
- python-dotenv
- webdriver-manager
- pandas
- openpyxl

---

## Installation

1. Clone the repository and save on your system
2. Create a virtual environment and activate it
3. Install Dependencies using command in your virtual environment: 
pip install -r requirements.txt
4. Create 2 directories in Project itself namely - logs and Data respectively and a .env file similar to .env.example
5. Change directory by - cd app/
6. Run - python -m main

---

## Further Scope Of Improvement

1. Speed boost using multithreading concurrency.
2. Multiple keywords and locations search simultaneously.
3. Automatic website crawling for fetching emails and other valuable data of a card listing.