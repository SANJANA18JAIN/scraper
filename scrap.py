import re
import sys
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from googlesearch import search

def extract_urls(query, max_urls=100):
    urls = []
    print("Starting Google search...")
    try:
        for url in search(query):
            if len(urls) >= max_urls:
                break
            print(f"Checking URL: {url}")
            if re.match(r'https://.*/arcgis/rest/services', url):
                if url not in urls:
                    urls.append(url)
                    print(f"Added URL: {url}")
            time.sleep(1)  # Sleep to avoid rate limiting
    except Exception as e:
        print(f"Error during Google search: {e}", file=sys.stderr)
    return urls

def scrape_href_attributes(urls):
    hrefs = []
    print("Scraping href attributes from URLs...")
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            for anchor in soup.find_all('a', href=True):
                href = anchor['href']
                if href.startswith('http'):  # Ensure it's an absolute URL
                    hrefs.append((url, href))
                    print(f"Found href: {href} in {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error scraping {url}: {e}", file=sys.stderr)
        time.sleep(1)  # Sleep to avoid rate limiting
    return hrefs

def add_column_if_not_exists(cursor, table_name, column_name, column_type):
    # Check if the column exists
    cursor.execute(f"""
        SELECT COUNT(*)
        FROM information_schema.columns
        WHERE table_name = '{table_name}' AND column_name = '{column_name}' AND table_schema = DATABASE();
    """)
    if cursor.fetchone()[0] == 0:
        # If the column does not exist, add it
        cursor.execute(f"ALTER TABLE {table_name} ADD {column_name} {column_type}")

def save_to_mysql(hrefs):
    import mysql.connector
    # Replace with your MySQL database connection details
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sanjana18jain28",
        database="scrapper"
    )
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INT AUTO_INCREMENT PRIMARY KEY
        )
    """)

    # Add columns if they do not exist
    add_column_if_not_exists(cursor, 'urls', 'base_url', 'VARCHAR(255)')
    add_column_if_not_exists(cursor, 'urls', 'href_url', 'VARCHAR(255)')

    # Insert URLs into the table
    for base_url, href_url in hrefs:
        cursor.execute("INSERT INTO urls (base_url, href_url) VALUES (%s, %s)", (base_url, href_url))

    conn.commit()
    cursor.close()
    conn.close()
    print("href attributes saved to MySQL database")

def main():
    query = "arcgis/rest/services"
    urls = extract_urls(query)
    
    hrefs = scrape_href_attributes(urls)
    
    # Save the href attributes to MySQL
    save_to_mysql(hrefs)

    print(f"Extracted {len(hrefs)} href attributes")

if __name__ == '__main__':
    main()
