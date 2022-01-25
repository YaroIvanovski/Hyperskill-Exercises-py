
hour = int(input())
minutes = int(input())
seconds = int(input())

hour2 = int(input())
minutes2 = int(input())
seconds2 = int(input())

result = (hour2 - hour) * 3600 + (minutes2 - minutes) * 60 + (seconds2 - seconds)
print(result)
