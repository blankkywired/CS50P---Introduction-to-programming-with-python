numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
user_input = (input('Expression: '))
print(user_input)
for num in numbers:
    if num in numbers:
        numbers.pop(num)
        num = str(num)
    numbers.append(num)
print(numbers)

