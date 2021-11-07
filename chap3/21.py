import json
import re

# これを解決するには、正規表現パターンに Python の raw 文字列記法を使います。
# 'r' を前置した文字列リテラル内ではバックスラッシュが特別扱いされません。
# 従って "\n" が改行一文字からなる文字列であるのに対して、 r"\n" は '\' と 'n' の二文字からなる文字列です。
# 通常、 Python コード中では、パターンをこの raw 文字列記法を使って表現します。

ans = []

with open("../public/jawiki-country.json") as f:
    for line in f:
        s = json.loads(line)
        if s["title"] == "イギリス":
            ans += s["text"].split("\n")

for line in ans:
    result = re.search('\[{2}Category:.+\]{2}', line)
    if result:
        print(result.group())