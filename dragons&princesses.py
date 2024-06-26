n = int(input())
dragons, princesses = [], []
gold, killed_dragons = 0, 0

# Чтение входных данных
for i in range(n-1):
    data = input().split()
    if data[0] == 'd':
        dragons.append((i + 2, data[1]))
    else:
        princesses.append((i + 2, data[1]))

princesses.sort(key=lambda x: x[1])
for princess in princesses:
    
    pass
