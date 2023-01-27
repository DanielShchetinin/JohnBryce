

error = "Error, Please try again"

while True:
    number = input("Please enter a number: ")
    if not number.isnumeric():
        print(error)
        continue
    else:
        number = int(number)
        new_number = str(number)
        static_str_number = str(number)
        break

Sum = 0
first = True
for i in range(0, number-1):
    Sum += int(new_number)
    if first is True:
        print(new_number, end = ' ')
        first = False
    new_number = new_number + static_str_number
    print("+", new_number, end = ' ')
print("=", Sum+int(new_number))