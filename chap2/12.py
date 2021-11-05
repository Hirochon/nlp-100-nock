import subprocess

# !cut -f 1 ./popular-names.txt > ./col1_chk.txt
# !cat ./col1_chk.txt | head -n 5

res = subprocess.check_output(["cut", "-f", "1", "../public/popular-names.txt"])
decodedRes = res.decode()

with open("../public/col1_chk.txt", "w") as f:
    f.write(decodedRes)

res2 = subprocess.check_output(["cut", "-f", "2", "../public/popular-names.txt"])
decodedRes2 = res2.decode()

with open("../public/col2_chk.txt", "w") as f:
    f.write(decodedRes2)
