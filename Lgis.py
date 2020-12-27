with open("rosalind_lgis.txt") as f:
    n = int(f.readline())
    pi = list(map(int, f.readline().split()))


def lgis():
    inc = []
    dec = []
    for i, a in enumerate(pi):
        inc.append(max([inc[j] for j, b in enumerate(pi[:i]) if b < a] or [[]], key=len) + [a])
    for i, a in enumerate(pi):
        dec.append(max([dec[j] for j, b in enumerate(pi[:i]) if b > a] or [[]], key=len) + [a])

    print(*max(inc, key = len))
    print(*max(dec, key = len))


lgis()

