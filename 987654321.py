N = int(input())

if N < 9:
    print(0)
elif N == 9:
    print(8)
else:
    print("72" + "0" * (N-10))
