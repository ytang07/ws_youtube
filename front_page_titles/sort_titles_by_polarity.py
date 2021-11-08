import json

with open("views_by_polarity.json", "r") as f:
    vbp = json.load(f)

with open("titles_and_views.json", "r") as f:
    tav = json.load(f)

sorted_tav = sorted(tav.items(), key=lambda kv:(kv[1]))
print(sorted_tav[-1])
print(vbp[sorted_tav[-1][0]])