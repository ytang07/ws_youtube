import matplotlib.pyplot as plt
import json

with open("views_by_polarity.json", "r") as f:
    entries = json.load(f)

polarities = []
vpds = []

for entry in entries:
    polarities.append(entries[entry]["polarity"])
    vpds.append(entries[entry]["views_per_day"])

plt.scatter(polarities, vpds)
plt.title("Views per Day by Polarity of Title")
plt.xlabel("Polarity of Title")
plt.ylabel("Views per Day")
plt.show()