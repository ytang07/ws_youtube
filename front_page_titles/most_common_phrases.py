import json
from text_api_config import headers, cw_url
import requests

with open("titles_and_views.json", "r") as f:
    tav = json.load(f)

sorted_tuples = sorted(tav.items(), key=lambda x:x[1], reverse=True)
for t in sorted_tuples:
    print(t)

exit()

text = ""
for t in tav:
    if "covid" in t.lower():
        continue
    text += t

print(text)

body = {
    "text": text
}

res = json.loads(requests.post(cw_url, headers=headers, json=body).text)
cws = res["most common phrases"]
print(cws)