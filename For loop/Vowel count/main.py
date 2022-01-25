
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0
for x in vowels:
    for y in string:
        if x == y:
            count += 1
print(count)
