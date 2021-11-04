import random

S = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sList = S.split()
sStart = sList[0]
sEnd = sList[-1]

sListKai = sList[1:-1]
ansList = []
chList = []
for s in sListKai:
    if len(s) > 4:
        ansList.append("")
        chList.append(s)
    else:
        ansList.append(s)

chList2 = chList[:]

chedList = []
for i in range(len(chList)):
    sIndex = random.randint(0, len(chList) - i - 1)
    chedList.append(chList2[sIndex])
    chList2.pop(sIndex)

print(sStart, end=" ")
i = 0
for s in ansList:
    if len(s) == 0:
        print(chedList[i], end=" ")
        i += 1
    else:
        print(s, end=" ")
print(sEnd)