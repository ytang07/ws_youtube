import re
import requests
import dateparser
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint
from bs4 import BeautifulSoup
import json

from text_api_config import headers, ner_url

chromedriver_path = "C:\\Users\\ytang\\Documents\\workspace\\teaching\\intermediate\\youtube\\front_page_titles\\chromedriver.exe"
service = Service(chromedriver_path)
chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(service=service, options=chrome_options)

home = "https://www.youtube.com/"
driver.get(home)
sleep(randint(2, 4))
# --------- run here and check for where to find videos ----------

soup = BeautifulSoup(driver.page_source, 'html.parser')
titles = soup.find_all("a", href=re.compile("watch.*"))
driver.quit()
# title, when uploaded, number of views
title_dict = {}
for title in titles:
    text = title.get('aria-label')
    if text is None:
        continue
    elements = text.split(' ')
    num_views = elements[-2]
    re_join = ' '.join(elements[:-2]).split('by')
    title_text = re_join[0]
    when_uploaded = re_join[1]
    body = {
        "text": when_uploaded
    }
    response = requests.post(ner_url, headers=headers, json=body)
    # {"ner":[["DATE","2 weeks ago"],["TIME","1 minute, 12 seconds"]]}
    x = re.findall(r"\"([0-9].*?)\"", response.text, re.DOTALL)
    try:
        y=x[0]
    except:
        continue
    # print(x[0])
    # print(f"{title_text}: {num_views}\nUploaded on: {when_uploaded}")
    title_dict[title_text] = (y, num_views)

title_to_avg_daily_views = {}
for title in title_dict:
    print(title)
    dt_object_then = dateparser.parse(title_dict[title][0])
    days_since = (datetime.datetime.now() - dt_object_then).days
    if days_since == 0:
        days_since = 1
    avg_views_per_day = int(title_dict[title][1].replace(',',''))/days_since
    print(avg_views_per_day)
    title_to_avg_daily_views[title] = avg_views_per_day

json_dict = json.dumps(title_to_avg_daily_views, indent=4)
with open("titles_and_views.json", "w") as f:
    f.write(json_dict)

# TODO: make polarity api return polarity scores

exit()