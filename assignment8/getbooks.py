'''
Task 3: Write a Program to Extract this Data + Task 4: Write out the Data
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

body = driver.find_element(By.CSS_SELECTOR, 'body')

results = []

li_entries = body.find_elements(
    By.CSS_SELECTOR,
    'li.row.cp-search-result-item[data-test-id="searchResultItem"]'
)


for li in li_entries:

 
    title_entry = li.find_element(By.CSS_SELECTOR, 'h3.cp-title')
    title = title_entry.text.strip()
   
    author_entries = li.find_elements(By.CSS_SELECTOR, 'span.cp-author-link')

    authors = []

    for author in author_entries:
        authors.append(author.text.strip())

    author_text = "; ".join(authors)

   
    format_year_div = li.find_element(By.CSS_SELECTOR, 'div.cp-format-info')

    format_year_span = format_year_div.find_element(
        By.CSS_SELECTOR,
        'span.display-info-primary'
    )

    format_year = format_year_span.text.strip()

    
    if "—" in format_year:
        format_year = format_year.split("—")[0].strip()

    result = {
        "Title": title,
        "Author": author_text,
        "Format-Year": format_year
    }
    results.append(result)

df = pd.DataFrame(results)
print(df)

#Task 4: Write out the Data

df.to_csv('python_homework/assignment8/get_books.csv', index=False)

with open('python_homework/assignment8/get_books.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, indent=4)

driver.quit()