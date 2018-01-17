diglist = []
with open("50dig") as digits:
    for line in digits:
        diglist.append(int(line.strip("\n")[0:11]))
print diglist
