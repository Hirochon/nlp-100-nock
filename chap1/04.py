S = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

nList = [1, 5, 6, 7, 8, 9, 15, 16, 19]

d = {}
for i, s in enumerate(S.split()):
    if i + 1 in nList:
        d[i+1] = s[0]
    else:
        d[i+1] = s[:2]
print(d)