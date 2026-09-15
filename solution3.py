n = int(input())
s = input()

def digit_sum(num_str):
    return sum(int(c) for c in num_str)

def check(x_str, y_str, z_str):
    if len(x_str) > 1 and x_str[0] == '0':
        return False
    if len(y_str) > 1 and y_str[0] == '0':
        return False
    if len(z_str) > 1 and z_str[0] == '0':
        return False
    y = int(y_str)
    z = int(z_str)
    return digit_sum(x_str) == y and digit_sum(y_str) == z

for i in range(1, n - 1):
    for j in range(i + 1, n):
        x_str = s[:i]
        y_str = s[i:j]
        z_str = s[j:]
        if check(x_str, y_str, z_str):
            print(x_str)
            exit()

print(-1)