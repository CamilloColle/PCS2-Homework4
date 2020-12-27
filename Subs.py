with open("rosalind_subs.txt") as f:
    s = f.readline().strip()
    sub = f.readline().strip()


def subs(s, sub):
    lst = []
    for i in range(len(s)):
        if s[i:].startswith(sub):
            lst.append(i + 1)

    return lst


print(*subs(s, sub))