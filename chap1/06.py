def wordBiGram(s):
    ss = s.replace(" ", "")
    rs = []
    for i in range(len(ss)-1):
        rs.append(ss[i:i+2])
    return rs

s1 = "paraparaparadise"
s2 = "paragraph"

s1BiGram = wordBiGram(s1)
s2BiGram = wordBiGram(s2)

ansWa = set(s1BiGram + s2BiGram)
print(ansWa)

ansSa1 = set(s1BiGram) - set(s2BiGram)
print(ansSa1)
ansSa2 = set(s1BiGram) - set(s2BiGram)
print(ansSa2)

ansSeki = ansWa - ansSa1 - ansSa2
print(ansSeki)
