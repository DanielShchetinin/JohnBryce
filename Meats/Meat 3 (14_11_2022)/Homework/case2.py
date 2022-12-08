#  Get an integer number from a user, and using a while loop print every third number starting from 1 up to the number inserted by the user.

number = int(input("Enter a number: "))
print_number = 0
while True:
    number_range = range(1, number)
    print(print_number)
    print_number += 3
    if print_number >= number:
        print(f"The last number: {number}")
        break
