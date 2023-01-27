# Write a program that continuously gets numbers from a user until he inserts an odd number.

odd_number = 1
even_number = 0
numbers = []
while True:
    get_number = input("Enter a number: ")
    if get_number.isdigit():
        number = get_number
        number = int(number)
        number %= 2
        if number == odd_number:
            break
        else:
            numbers.append(get_number)
    else:
        print("Error, Enter only a digit!!!")
        continue
        
print(f"Your numbers: {numbers}")