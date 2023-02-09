numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
print(numbers)
comparison_last = 0

for number in numbers:
    if number > comparison_last:
        comparison_last = number
print(numbers)
print(comparison_last)
