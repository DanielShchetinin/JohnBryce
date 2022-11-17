
# Here we get a numbers from a user.
first_num = int(input("Your need enter a 3 number to get a average\n Enter your first number: "))
second_num = int(input("Enter your second number: "))
third_num = int(input("Enter your third number: "))

# Here we get a total number from user's numbers and do average.
numbers = first_num + second_num + third_num
average = numbers / 3

# Here we send a result to the user.
print(f"Your numbers togethere is - {numbers}.\nYour average is - {average}.")