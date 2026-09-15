x = int(input())
y = int(input())

a = 2*y - x
b = 2*x - y

print("Yes") if a >= 0 and b >= 0 and a % 3 == 0 and b % 3 == 0 else print("No")