S = "I am Hirochon"

def cipher(s: str):
    rs = [chr(219 - ord(ss)) if ss.islower() else ss for ss in s]
    return ''.join(rs)

S = cipher(S)
print(S)
S = cipher(S)
print(S)