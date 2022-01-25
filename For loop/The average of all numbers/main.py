
first = int(input())
second = int(input())
num_sum = 0
avg = 0
count = 0
for i in range(first, second + 1):
    if i % 3 == 0:
        num_sum += i
        count += 1
print(num_sum / count)
