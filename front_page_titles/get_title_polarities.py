import requests
import json
from text_api_config import apikey

with open("titles_and_views.json", "r") as f:
    entries = json.load(f)

def get_polarity(entry):
    headers = {
        "Content-Type": "application/json",
        "apikey": apikey
    }
    body = {
        "text": entry
    }
    url = "https://app.thetextapi.com/text/text_polarity"
    res = json.loads(requests.post(url, headers=headers, json=body).text)
    _p = res["text polarity"]
    return(_p)

# get the polarity of each title
# compare the polarity to the views per day
# plot the polarity against views per days
new_doc = {}
i = 0
for entry in entries:
    _p = get_polarity(entry)
    _vpd = entries[entry]
    _dict = {
        "polarity": _p,
        "views_per_day": _vpd
    }
    new_doc[entry] = _dict

json_dict = json.dumps(new_doc, indent=4)
with open("views_by_polarity.json", "w") as f:
    f.write(json_dict)
    