def pow(val, p):
    s, v, c = 1, val, p
    while (c != 0):
        if (c % 2 == 1):
            s = s * v
        c = c >> 1
        v = v * v
    return s


a, b = map(int, input().split())
print(pow(a, b) - pow(b, a))
