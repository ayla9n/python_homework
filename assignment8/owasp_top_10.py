'''
Task 6: Scraping Structured Data
extract the top 10 security risks reported on [https://owasp.org/www-project-top-ten/]
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("https://owasp.org/www-project-top-ten/")

top_10_list = []  

current_version_link = driver.find_element(
    By.XPATH,
    '//p[contains(text(), "The most current released version")]//a'
)

#gets url for the current version for the top 10 list
current_version_url = current_version_link.get_attribute("href")

driver.get(current_version_url)

top_10_h3 = driver.find_element(By.XPATH, '//h3[contains(@id, "top-10")]')

if top_10_h3:
    top_10_ol = top_10_h3.find_element(By.XPATH, 'following-sibling::ol') 

    link_elements = top_10_ol.find_elements(By.CSS_SELECTOR, 'a')  
    for link in link_elements:
        title = link.text.strip()
        url = link.get_attribute("href")

        if title and url:
            print(f"{title}: {url}")

            top_10_list.append({  
                "Title": title,
                "Link": url
            })

df = pd.DataFrame(top_10_list)  

print(df)

df.to_csv("owasp_top_10.csv", index=False)

driver.quit()