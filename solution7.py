n = int(input())
cars = list(map(int, input().split()))

dead1 = []
dead2 = []
commands = []
next_out = 1
idx = 0

while next_out <= n:
    while True:
        if dead1 and dead1[-1] == next_out:
            commands.append(-1)
            dead1.pop()
            next_out += 1
        elif dead2 and dead2[-1] == next_out:
            commands.append(-2)
            dead2.pop()
            next_out += 1
        else:
            break

    if next_out > n:
        break

    if idx < n:
        car = cars[idx]
        idx += 1
        if not dead1 or dead1[-1] > car:
            commands.append(1)
            dead1.append(car)
        else:
            commands.append(2)
            dead2.append(car)
    else:
        if dead1 and dead1[-1] != next_out:
            commands.append(12)
            dead2.append(dead1.pop())
        elif dead2 and dead2[-1] != next_out:
            commands.append(21)
            dead1.append(dead2.pop())

print('\n'.join(map(str, commands)))