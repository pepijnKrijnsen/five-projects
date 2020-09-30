# WEB SCRAPER 101
#
# What is it:
# - Automation engine to get data from websites and either store it for later
# parsing, or act on it immediately
#

import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.ie/jobs/search/?q=python-developer&cy=ie"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

jobs = results.find_all("section", class_="card-content")

for job in jobs:
    title_elem = job.find("h2", class_="title")
    company_elem = job.find("div", class_="company")
    location_elem = job.find("div", class_="location")
    date_elem = job.find("div", class_="meta flex-col")
    if None in (title_elem, company_elem, location_elem, date_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(date_elem.text.strip())
    print()
