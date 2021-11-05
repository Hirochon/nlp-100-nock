import subprocess
from collections import defaultdict

res = subprocess.check_output(["cut", "-f", "1", "../public/popular-names.txt"])
decodedRes = res.decode()

dd = defaultdict(int)

for d in decodedRes.split():
    dd[d] += 1

nd = []
for d, d2 in dd.items():
    nd.append((d2, d))
print(sorted(nd)[::-1])