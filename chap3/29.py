import json
import re
import requests

with open("../public/jawiki-country.json") as f:
    for line in f:
        s = json.loads(line)
        if s["title"] == "イギリス":
            S = s["text"]

result = re.findall("\{\{基礎情報.+?^\}\}", S, re.MULTILINE + re.DOTALL)

ans = {}

for res in result[0].split("\n"):
    # print(res)
    r = re.findall("^\|(.+)\s=\s(.+)", res)
    if len(r) > 0:
        r = r[0]
        ans[r[0]] = r[1]

text = ans["国旗画像"].replace(" ", "_")
res = requests.get("https://commons.wikimedia.org/w/api.php?action=query&titles=File:" + text + "&prop=imageinfo&iiprop=url&format=json")
response = json.loads(res.text)
print(response["query"]["pages"]["347935"]["imageinfo"][0]["url"])