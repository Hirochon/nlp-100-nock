import subprocess

res = subprocess.check_output(["cut", "-f", "1", "../public/popular-names.txt"])
decodedRes = res.decode()
print(set(decodedRes.split()))
