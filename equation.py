def gcd(a,b):
    while b > 0:
        a %= b
        a, b = b, a
    return a


a, b, c = map(int, input().split())
x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
cnt = 0

if not a and not b:
    if not c:
        cnt = (x2 - x1 + 1) * (y2 - y1 + 1)
elif not b:
    if (c / a).is_integer() and x1 <= c / a <= x2:
        cnt = y2 - y1 + 1
elif not a:
    if (c / b).is_integer() and y1 <= c / b <= y2:
        cnt = x2 - x1 + 1
else:
    gcd = gcd(abs(a), abs(b))
    if (c / gcd).is_integer():
        a //= gcd
        b //= gcd
        c //= gcd
        x01 = - (c + b * y1) // a
        x02 = - (c + b * y2) // a
        x01, x02 = min(x01, x02), max(x01, x02)
        x01, x02 = max(x01, x1), min(x02, x2)
        for x in range(x01, x02 + 1):
            y = - (c + a * x) / b
            if y.is_integer() and y1 <= y <= y2:
                dx = x2 - x
                if a * b > 0:
                    dy = int(y) - y1
                else:
                    dy = y2 - int(y)
                cnt = min(dx // abs(b), dy // abs(a)) + 1
                break
print(cnt)
