from collections import deque

a = int(input())
b = int(input())

queue = deque([(0, 0, 0)])
parent = {(0, 0, 0): None}
ans_state = None

while queue:
    sx, s2x, c = queue.popleft()

    if sx == a and s2x + c == b:
        ans_state = (sx, s2x, c)
        break

    for d in range(10):
        nsx = sx + d
        if nsx > a:
            continue

        val = 2 * d + c
        nc, digit_2x = val // 10, val % 10
        ns2x = s2x + digit_2x

        if ns2x + nc > b:
            continue

        nxt = (nsx, ns2x, nc)
        if nxt not in parent:
            parent[nxt] = (sx, s2x, c, d)
            queue.append(nxt)

if ans_state is None:
    print(-1)
else:
    digits = []
    curr = ans_state
    while parent[curr] is not None:
        px, ps2x, pc, d = parent[curr]
        digits.append(str(d))
        curr = (px, ps2x, pc)

    res = "".join(reversed(digits)).lstrip("0")
    print(res if res else -1)