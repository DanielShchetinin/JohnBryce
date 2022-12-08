# Find the factorial of a given number.
# Take into account that factorial of 0 is 1, and factorial does not exist for negative numbers.

count = 1
num = int(input("Please enter a number: "))
for i in range(0, 10):
    print(count,"*",num, "=", count*num )
    count += 1