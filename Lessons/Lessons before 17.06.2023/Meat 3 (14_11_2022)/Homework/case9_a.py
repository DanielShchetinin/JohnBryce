while True:
    number = input("Enter a number: ")
    if not number.isdigit:
        print("Error, Try again!")
        continue
    else:
        print(number[::-1])