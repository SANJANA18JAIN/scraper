## scraper
This file includes instructions on setting up the environment, installing dependencies, running the script, and details about the project.

# URL Scraper

This project is a Python script that performs a Google search for URLs containing the path "arcgis/rest/services", scrapes href attributes from these URLs, and saves the data to a MySQL database.

## Features

- Performs Google search for specified query
- Extracts URLs containing "arcgis/rest/services"
- Scrapes href attributes from the extracted URLs
- Saves the data to a MySQL database

## Requirements

- Python 3.x
- MySQL

2. Set Up a Virtual Environment
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use .\env\Scripts\activate
   ```

3. Install Dependencies
   sh
   pip install -r requirements.txt
   

4. Create MySQL Database
   - Create a MySQL database named `scrapper`
   - Update the MySQL connection details in the script

5. Run the Script
   sh
   python scrap.py
   

## Configuration

Update the MySQL connection details in the `save_to_mysql` function in `scrape_urls.py`:
python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="scrapper"
)

## Usage

The script performs the following steps:

1. Extracts URLs from Google search results.
2. Scrapes href attributes from the extracted URLs.
3. Saves the href attributes to a MySQL database.

## Script Breakdown

### `extract_urls(query, max_urls=100)`

This function performs a Google search for the specified query and extracts up to `max_urls` URLs that contain "arcgis/rest/services".

### `scrape_href_attributes(urls)`

This function scrapes href attributes from the given list of URLs.

### `add_column_if_not_exists(cursor, table_name, column_name, column_type)`

This function checks if a column exists in a table, and if not, adds the column.

### `save_to_mysql(hrefs)`

This function saves the base URLs and href attributes to a MySQL database.

### `main()`

The main function orchestrates the entire process:
1. Performs the Google search.
2. Scrapes href attributes.
3. Saves the data to the MySQL database.

### Explanation

1. Introduction: Provides an overview of the project and its features.
2. Requirements Lists the software and tools needed to run the project.
3. Setup and Installation: Step-by-step instructions on how to clone the repository, set up a virtual environment, install dependencies, and create a MySQL database.
4. Configuration: Instructions for updating the MySQL connection details in the script.
5. Usage: Describes what the script does and the order of operations.
6. Script Breakdown: Explains the functions in the script and their roles.
7. Contributing: Invites contributions and explains how to submit pull requests.
8. License: Indicates the project is licensed under the MIT License.
9. Contact: Provides contact information for questions or issues.

