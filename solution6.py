n = int(input())
row0 = input()
row1 = input()

dominoes = []
i = 0
while i < n:
    if row0[i] == row1[i]:
        dominoes.append(('V', i, i))
        i += 1
    else:
        dominoes.append(('H', i, i + 1))
        i += 2

def other_colors(c):
    return [x for x in range(3) if x != c]


def colors_not(excluded):
    return [x for x in range(3) if x not in excluded]

first = dominoes[0]
if first[0] == 'V':
    dp = {('V', c): 1 for c in range(3)}
else:
    dp = {('H', t, b): 1 for t in range(3) for b in range(3) if t != b}

for idx in range(1, len(dominoes)):
    dom = dominoes[idx]
    prev = dominoes[idx - 1]
    new_dp = {}

    if dom[0] == 'V':
        for c in range(3):
            total = 0
            if prev[0] == 'V':
                for state, cnt in dp.items():
                    if state[1] != c:
                        total += cnt
            else:
                for state, cnt in dp.items():
                    pt, pb = state[1], state[2]
                    if c != pt and c != pb:
                        total += cnt
            if total:
                new_dp[('V', c)] = total
    else:
        # new horizontal pair
        for t in range(3):
            for b in range(3):
                if t == b:
                    continue
                total = 0
                if prev[0] == 'V':
                    for state, cnt in dp.items():
                        pc = state[1]
                        if t != pc and b != pc:
                            total += cnt
                else:
                    for state, cnt in dp.items():
                        pt, pb = state[1], state[2]
                        if t != pt and b != pb:
                            total += cnt
                if total:
                    new_dp[('H', t, b)] = total
    dp = new_dp

print(sum(dp.values()))