n, m = map(int, input().split())

table = list()
for _ in range(n):
    table.append(list(input()))

for col in range(m):
    letters = [table[row][col] for row in range(n) if table[row][col] != '.']
    for row in range(n):
        if row < n - len(letters):
            table[row][col] = '.'
        else:
            table[row][col] = letters[row - (n - len(letters))]

for row in table:
    print(''.join(row))