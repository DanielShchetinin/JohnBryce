error = "Error, Please try again"
space = ' '

while True:
    number = input("Please enter a number: ")
    if not number.isnumeric():
        print(error)
        continue
    else:
        number = int(number)
        break
    
for i in range(1, number+1):
     print(i*'*')
     number -= 1
     i+=1