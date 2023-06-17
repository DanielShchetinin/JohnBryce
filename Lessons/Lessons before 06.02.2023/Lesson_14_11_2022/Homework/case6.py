# Write a program that receives 10 strings from a user, and prints the amount of strings with even length.

error = 'Error, Please try again'
count = 0
words = 0

while True:
    word = input(f'Enter a words [{count}/10]: ')
    number = len(word) % 2
    if count == 10:
        break
    print(number)
    
    if number == 0:
        words += 1
        count += 1
        continue
    else:
        count += 1

print(f"Amount of the even lengh: {words}")