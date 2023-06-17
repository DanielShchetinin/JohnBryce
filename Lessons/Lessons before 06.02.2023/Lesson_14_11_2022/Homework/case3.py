# Get numbers from the user until you get a special char indicating the end of input, and print the sum and the average of the numbers.

count = 0
numbers = 0
while True:
    number = input("Enter your numbers (For stop insert - $): ")
    if number == '$':
        break
    if number.isdigit():
        number = int(number)
        numbers += number
        count += 1
        continue
    
print(f"\nYou stop the process and get a result!")
print(f"Sum of your numbers: {numbers}.\nAverage of your numbers: {numbers / count}.\n")