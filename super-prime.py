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


def fi_max(n, super_prime, gl):
    if gl < 0:
        return 0
    elif n == 0:
        return 1
    elif n < 3:
        return 0
    elif len(super_prime):
        a = n
        cnt = 0
        while a >= super_prime[-1]:
            cnt += 1
            a -= super_prime[-1]
        agl = gl - cnt
        if not fi_max(a, super_prime[:-1], agl):
            super_prime = super_prime[:-1]
            if len(super_prime):
                return fi_max(n, super_prime, gl)
            else:
                return 0
        else:
            if cnt:
                global sp2
                for i in range(cnt):
                    sp2.append(super_prime[-1])
            return 1
    else:
        return 0


n = int(input())
a = list(range(n + 1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n + 1, i):
            a[j] = 0
    i += 1

super_prime = []
for i in range(len(lst)):
    if i + 1 in lst:
        super_prime.append(lst[i])

sp = []
if not finder(n, super_prime):
    print(0)
else:
    sp2 = []
    while fi_max(n, super_prime, len(sp) - 1):
        sp = sp2
        sp2 = []
    print(len(sp))
    print(*sp)
