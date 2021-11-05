import subprocess

N = int(input())

res = subprocess.check_output(["tail", "-n", str(N), "../public/popular-names.txt"])
decodedRes = res.decode()
print(decodedRes)
