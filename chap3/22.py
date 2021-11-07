import json
import re

with open("../public/jawiki-country.json", "r") as f:
    for line in f:
        s = json.loads(line)
        if s["title"] == "イギリス":
            S = s["text"]

for s in S.split("\n"):
    result = re.search('\[{2}Category:.+\]{2}', s)
    if result:
        # print(result.group(0))
        res = re.sub('\[{2}Category:(.+)\]{2}', '\\1', result.group(0))
        print(res)