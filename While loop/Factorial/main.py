
num = int(input())
while True:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(fact)
    break

"""
num = int(input())
counter = 0
fact = 1
while counter < num:
    counter += 1
    fact *= counter
print(fact)
"""
