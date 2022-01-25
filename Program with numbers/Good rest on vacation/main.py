
days = int(input())
food = int(input())
flight = int(input())
hotel = int(input())

res = hotel * (days - 1) + food * days + flight * 2
print(res)
