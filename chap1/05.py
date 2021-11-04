S = "I am an NLPer"

def wordBiGram(s):
    ss = s.replace(" ", "")
    rs = []
    for i in range(len(ss)-1):
        rs.append(ss[i:i+2])
    return rs

print(wordBiGram(S))

def sentenseBiGram(s):
    sList = s.split()
    rs = []
    for i in range(len(sList)-1):
        rs.append(sList[i] + sList[i+1])
    return rs

print(sentenseBiGram(S))