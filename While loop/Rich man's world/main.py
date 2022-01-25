
deposit = int(input())
years = 0
limit = 700000
rate = 7.1
while deposit < limit:
    interest = deposit * rate / 100
    deposit += interest
    years += 1
print(years)
