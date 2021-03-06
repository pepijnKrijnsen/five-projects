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
from lxml import html 

county = "Limerick"
URL = "https://www.monster.ie/jobs/search/?q=python-developer&cy=ie&stpage=1&page=6"

page = requests.get(URL)
doc = html.fromstring(page.content)

results = {}

job_title_sections = doc.xpath("//*[@id='SearchResults']/section/@data-jobid")

i = 0
for section_id in job_title_sections:
    i += 1
    job_title_name = doc.xpath("//*[@data-jobid={}]/div/div[2]/header/h2/a/text()".format(section_id))
    if job_title_name:
        job_title_links = doc.xpath("//*[@data-jobid={}]/div/div[2]/header/h2/a/@href".format(section_id))
        job_location = doc.xpath("//*[@id='SearchResults']/section/div/div[2]/div[2]/a/text()")
        nll_list = []
        nll_list.append(job_title_name)
        nll_list.append(job_title_links)
        nll_list.append(job_location)
        results[section_id] = nll_list
    if i == 8:
        quit()

print(results)

# job_title_links = doc.xpath("//*[@data-jobid={}]/div/div[2]/header/h2/a/@href".format(section_id))
# job_title_names = doc.xpath("//*[@id='SearchResults']/section/div/div[2]/header/h2/a/text()")
# job_location = doc.xpath("//*[@id='SearchResults']/section/div/div[2]/div[2]/a/text()")



intro = """
################################
JOB OVERVIEW
################################
"""
preferred_county = "Jobs in {}\n".format(county)

# i = 0
# for v in job_location:
#     i += 1
#     print(v)
#     if county in v:
#         results = job_title_links[i] + ", " + job_location[i] + "\n"
# 
# print(intro)
# print(preferred_county)
# print(results)
