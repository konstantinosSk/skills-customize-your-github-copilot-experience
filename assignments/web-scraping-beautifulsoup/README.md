# 📘 Assignment: Web Scraping with BeautifulSoup

## 🎯 Objective

Learn to extract data from websites using BeautifulSoup and HTTP requests. You'll fetch web pages, parse HTML structures, and extract meaningful data. By completing this assignment, you'll understand how to automate data collection from websites and prepare datasets for analysis, all while practicing ethical web scraping principles.

## 📝 Tasks

### 🛠️ Fetch Web Pages and Parse HTML

#### Description
Write code to download a web page and extract structured data by parsing its HTML. This is the foundation of web scraping—retrieving and understanding web content.

#### Requirements
Completed program should:

- Use the `requests` library to fetch a web page
- Parse the HTML using BeautifulSoup
- Inspect the page structure to identify CSS selectors or HTML tags
- Print or display extracted elements to verify parsing works correctly
- Handle network errors gracefully (e.g., connection timeouts)

### 🛠️ Extract and Organize Data

#### Description
Target specific data elements from the parsed HTML and organize them into a structured format. Extract multiple pieces of information from each item on the page.

#### Requirements
Completed program should:

- Use CSS selectors or tag searches to locate specific data
- Extract multiple attributes from each item (e.g., title, link, date, price)
- Store extracted data in a list of dictionaries or a similar structure
- Handle missing or malformed data gracefully
- Display or save the organized data

### 🛠️ Process Multiple Pages and Build Datasets

#### Description
Scale your scraper to handle pagination and collect data across multiple pages. Build complete datasets for analysis or storage.

#### Requirements
Completed program should:

- Implement logic to loop through multiple pages or pagination links
- Aggregate data from all pages into a single dataset
- Export data to a CSV or JSON file
- Implement reasonable delays between requests to avoid overloading the server
- Include error handling for failed requests on individual pages

### 🛠️ Respect Web Standards and Ethics (Stretch Goal)

#### Description
Implement best practices for responsible web scraping, including checking robots.txt and respecting server resources.

#### Requirements
Completed program should:

- Check the website's `robots.txt` file to ensure scraping is allowed
- Set an appropriate User-Agent header in requests
- Implement rate limiting (delays between requests)
- Log scraping activity for monitoring
- Handle HTTP status codes appropriately (403 Forbidden, 429 Too Many Requests, etc.)
- Document the data source and scraping timestamp in exported files
