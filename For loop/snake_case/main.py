
camel_case = input()
snake_case = []

for letter in camel_case:
    if letter.islower():
        snake_case.append(letter)
    else:
        snake_case.append("_")
        snake_case.append(letter.lower())
print("".join(snake_case))
