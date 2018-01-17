def rotations(n):
    S=[]
    n = str(n)
    for i in range(len(n)):
        S.append(int(n[i:]+n[:i]))
    return list(set(S))
