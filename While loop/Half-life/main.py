
initial = int(input())
final = int(input())
days = 12
count = 0

while initial > final:
    initial /= 2
    count += 1

print(days * count)
