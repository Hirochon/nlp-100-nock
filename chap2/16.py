import subprocess

N = 2780 // int(input())

res = subprocess.check_output(["split", "-l", str(N), "-d", "../public/popular-names.txt", "sp"])
decodedRes = res.decode()
print(decodedRes)
