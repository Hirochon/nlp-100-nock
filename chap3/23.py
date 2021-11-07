import json
import re

with open("../public/jawiki-country.json") as f:
    for line in f:
        s = json.loads(line)
        if s["title"] == "イギリス":
            S = s["text"]

for s in S.split("\n"):
    result = re.search("==.+==", s)
    if result:
        print(result.group(), end="")
        res = re.findall("=", result.group())
        print(" level:", len(res)//2-1, sep="")