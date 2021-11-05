import subprocess

res = subprocess.check_output(["paste", "../public/col1_chk.txt", "../public/col2_chk.txt"])
decodedRes = res.decode()
print(decodedRes)
