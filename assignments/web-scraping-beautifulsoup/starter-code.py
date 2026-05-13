"""
Web Scraping with BeautifulSoup - Starter Code

This file provides a basic structure to help you get started with web scraping.
Fill in the missing implementations to complete the assignment tasks.

Requirements:
- pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
from typing import List, Dict
from urllib.parse import urljoin, urlparse

# Set up a session for better performance and to persist cookies
session = requests.Session()
session.headers.update({
    'User-Agent': 'Educational Web Scraper (Learning Project)'
})

# Configuration
BASE_URL = "https://example.com"  # TODO: Replace with your target website
DELAY_BETWEEN_REQUESTS = 1  # seconds - be respectful to the server


def fetch_page(url: str) -> BeautifulSoup:
    """
    Fetch a web page and return a BeautifulSoup object for parsing.
    
    TODO: Implement this function to:
    1. Make an HTTP request to the URL
    2. Check for errors (non-200 status codes)
    3. Parse the response with BeautifulSoup
    4. Return the BeautifulSoup object
    """
    pass


def extract_items(soup: BeautifulSoup) -> List[Dict]:
    """
    Extract items from a parsed HTML page.
    
    TODO: Implement this function to:
    1. Find all item containers using CSS selectors or tag searches
    2. Loop through each item and extract relevant data
    3. Store data in a list of dictionaries
    4. Return the list of extracted items
    
    Example item structure:
    [
        {'title': '...', 'link': '...', 'description': '...'},
        {'title': '...', 'link': '...', 'description': '...'},
    ]
    """
    pass


def scrape_multiple_pages(base_url: str, num_pages: int) -> List[Dict]:
    """
    Scrape data from multiple pages of a website.
    
    TODO: Implement this function to:
    1. Loop through each page number
    2. Construct the URL for each page (pagination)
    3. Call fetch_page() and extract_items() for each page
    4. Add a delay between requests (DELAY_BETWEEN_REQUESTS)
    5. Aggregate all items into a single list
    6. Return the complete dataset
    """
    pass


def save_to_csv(data: List[Dict], filename: str = 'scraped_data.csv') -> None:
    """
    Save scraped data to a CSV file.
    
    TODO: Implement this function to:
    1. Check that data is not empty
    2. Get the fieldnames from the first item's keys
    3. Write the data to a CSV file using csv.DictWriter
    4. Include a timestamp in the output (for documentation)
    """
    pass


def check_robots_txt(base_url: str) -> bool:
    """
    Check the website's robots.txt to see if scraping is allowed.
    (Stretch goal)
    
    TODO: Implement this function to:
    1. Construct the robots.txt URL
    2. Fetch the robots.txt file
    3. Check if scraping is allowed for your User-Agent
    4. Return True if allowed, False otherwise
    """
    pass


def main():
    """
    Main function to orchestrate the scraping process.
    """
    try:
        # Task 1: Fetch and parse a single page
        print("Fetching and parsing web page...")
        soup = fetch_page(BASE_URL)
        
        # Task 2: Extract data from the page
        print("Extracting items from page...")
        items = extract_items(soup)
        print(f"Found {len(items)} items")
        
        # Task 3: Scrape multiple pages (optional)
        print("Scraping multiple pages...")
        all_items = scrape_multiple_pages(BASE_URL, num_pages=3)
        print(f"Total items scraped: {len(all_items)}")
        
        # Task 4: Save to CSV
        print("Saving data to CSV...")
        save_to_csv(all_items)
        print("Done! Data saved to 'scraped_data.csv'")
        
    except Exception as e:
        print(f"Error during scraping: {e}")


if __name__ == "__main__":
    main()
