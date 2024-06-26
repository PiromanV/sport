'''
def finder(n, super_prime):
    if n == 0:
        return 1
    elif n < 3:
        return 0
    elif len(super_prime):
        a = n
        cnt = 0
        while a >= super_prime[-1]:
            cnt += 1
            a -= super_prime[-1]
        if not finder(a, super_prime[:-1]):
            super_prime = super_prime[:-1]
            if len(super_prime):
                return finder(n, super_prime)
            else:
                return 0
        else:
            if cnt:
                global sp
                for i in range(cnt):
                    sp.append(super_prime[-1])
            return 1
    else:
        return 0


def finder2(n, super_prime):
    if n == 0:
        return 1
    elif n < 3:
        return 0
    elif len(super_prime):
        a = n
        b = n//2
        k = super_prime[0]
        i = 0
        while k < b and i < len(super_prime) - 1:
            i += 1
            k = super_prime[i]
        cnt = 0
        while a >= k:
            cnt += 1
            a -= k
        if not finder2(a, super_prime[:-1]):
            super_prime = super_prime[:-1]
            if len(super_prime):
                return finder2(n, super_prime)
            else:
                return 0
        else:
            if cnt:
                global sp
                for i in range(cnt):
                    sp.append(k)
            return 1
    else:
        return 0

for n in range(2, 1000):
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1

    super_prime = []
    for i in range(len(lst)):
        if i + 1 in lst:
            super_prime.append(lst[i])

    sp = []
    print(n)
    if not finder2(n, super_prime):
        print(0,"\n\n\n")
    else:
        print(len(sp))
        print(*sp)
'''

def asum(sum_list, n):
    s = 0
    for i in range(n):
        s += sum_list[i]
    return s


n = int(input())
sum_list = [0] * 100
xn = 0

a = list(range(n+1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1

super_prime = []
for i in range(len(lst)):
    if i + 1 in lst:
        super_prime.append(lst[i])


for i in range(len(super_prime)):
    if asum(sum_list, xn) + super_prime[i] <= n:
        sum_list[xn] = super_prime[i]
        xn += 1
    if asum(sum_list, xn) == n:
        break

if asum(sum_list, xn) < n:
    print(0)
else:
    for i in range(xn):
        print(sum_list[i], end=" ")
