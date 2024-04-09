numbers = [4, 5, 3, 7, -1, -2, 1, -6]
print(numbers)
for j in range(len(numbers) - 1):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    print(numbers)