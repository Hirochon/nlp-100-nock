import subprocess

res = subprocess.check_output(["cut", "-f", "3", "../public/popular-names.txt"])
decodedRes = res.decode()
print(sorted(list(map(int, decodedRes.split()))))
