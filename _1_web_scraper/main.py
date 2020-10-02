# WEB SCRAPER 101
#
# What is it:
# - Automation engine to get data from websites 
# What's the use case:
# - Getting data from a website that doesn't have a public API
# 
# Goal of this script:
# - To get a list of all Python developer jobs from the Monster.ie job site.
# I get an email from them every day listing developer jobs, but they usually
# list exactly the same jobs multiple days in a row even if newer jobs are
# available (presumably because those recruiters pay more).

import requests
from os import path
from lxml import html, etree

county = "county__3AClare"
URL = "https://www.monster.ie/jobs/search/?q=python-developer&where={}&cy=ie".format(county)

page = requests.get(URL)
doc = html.fromstring(page.content)

job_titles = doc.xpath("//*[@id='SearchResults']/section/div/div[2]/header/h2/a/text()")
for v in job_titles:
    print(v)

print("Aww, YISSSSSS")
