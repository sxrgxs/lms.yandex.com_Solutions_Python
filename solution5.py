n, m = map(int, input().split())
names = [input() for _ in range(n)]

result = []
for j in range(m):
    freq = {}
    for i in range(n):
        c = names[i][j]
        freq[c] = freq.get(c, 0) + 1
    result.append(max(freq, key=freq.get))

print(''.join(result))