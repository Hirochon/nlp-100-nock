import json
import re

with open("../public/jawiki-country.json") as f:
    for line in f:
        s = json.loads(line)
        if s["title"] == "イギリス":
            S = s["text"]

result = re.findall("\{\{基礎情報.+?^\}\}", S, re.MULTILINE + re.DOTALL)

a = {}

for res in result[0].split("\n"):
    # print(res)
    r = re.findall("^\|(.+)\s=\s(.+)", res)
    if len(r) > 0:
        r = r[0]
        a[r[0]] = r[1]

ans = []

for k, v in a.items():
    nV = re.sub("\'{2,5}", "", v)
    ans.append(k + " : " + nV)

print(ans)