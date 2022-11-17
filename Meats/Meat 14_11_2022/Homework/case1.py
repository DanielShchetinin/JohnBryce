numbers = []
count = 0
while True:
    if count >= 10:
        break
    number = int(input("Enter a number to the list: "))
    numbers.append(number)
    count += 1
print(numbers)
print(count)