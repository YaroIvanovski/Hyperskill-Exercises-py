
i = 0
count = 0
num = int(input())
average = 0
limit = 55

while num != limit:
    i += 1
    count += num
    average = count / i
    num = int(input())

print(i)
print(count)
print(round(average))
