s = input()
n = len(s)


def solve(pos, used):
    if pos == n:
        return []

    for length in range(1, 3):
        if pos + length > n:
            break
        token = s[pos:pos + length]
        if length > 1 and token[0] == '0':
            continue
        num = int(token)
        if 1 <= num <= 50 and num not in used:
            result = solve(pos + length, used | {num})
            if result is not None:
                return [num] + result
    return None

print(*solve(0, set()))