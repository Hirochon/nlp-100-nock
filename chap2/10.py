import subprocess

res = subprocess.check_output(["wc", "../public/popular-names.txt"])

print(str(res).split()[1])
