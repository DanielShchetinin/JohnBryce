

error = "Error, Please try again"

while True:
    number = input("Please enter a number: ")
    if not number.isnumeric():
        print(error)
        continue
    else: 
        number = int(number)
        break
        
for i in range(1, number+1):
    print(f"Current Number is: {i} and the cube is {i**3}")
    i += 1