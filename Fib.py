with open('rosalind_fib.txt') as f:
    r = f.readline().split()

m = int(r[0])
k = int(r[1])


def fib(m, k):
    old = new = 1
    for i in range(1, m):
        new, old = old, old + (new*k)

    return new


print(fib(m, k))
