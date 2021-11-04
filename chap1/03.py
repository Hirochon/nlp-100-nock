s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

sList = s.split()
for s in sList:
    s = s.replace(",", "")
    s = s.replace(".", "")
    print(len(s))
