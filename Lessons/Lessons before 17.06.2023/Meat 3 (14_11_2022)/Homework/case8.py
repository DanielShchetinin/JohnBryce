# Write a program that counts the total number of digits in a number received from a user using a while loop.

total = 0

while True:
    number = input(f"Enter your number [Total now: {total}]: ")
    if number == '$':
        break
    if not number.isdigit():
        print('Error, Try again and insert only numbers!')
        continue
    else:
        number = int(number)
        total += number
    
print(f"Your total numbers: {total}")