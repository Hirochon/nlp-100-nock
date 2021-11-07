import json
import re

with open("../public/jawiki-country.json") as f:
    for line in f:
        s = json.loads(line)
        if s["title"] == "イギリス":
            S = s["text"]


result = re.findall('\[{2}ファイル:(.+?)\|', S)
print(len(result))
for res in result:
    print(res)