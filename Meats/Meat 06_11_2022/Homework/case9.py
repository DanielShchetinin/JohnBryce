number = input("Enter a number to swip: ")
if number < 10 or number > 99 + 1:
    print("error")
print(f"Your swiped number is {number[::-1]}")