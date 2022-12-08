# Write a program that receives strings from a user until the user inserts a special character $ that indicates the end of the input.
# After $ has been inserted, the program should print out the total number of strings inserted by the user, total number of all the characters inserted by the user, and total number of digits inserted by the user (in strings that contain digits only).

count = 0
letters = 0
numbers = 0

while True:
    word = input("Enter some words or nubmers: ")
    if word == '$':
        break
    if word.isdigit():
        letters += len(word)
        word = int(word)
        count += 1
        numbers += word
    else:
        count += 1
        letters += len(word)
        
print(f"Sum of words: {count}")
print(f"Sum of letters: {letters}")
print(f"Sum of numbers: {numbers}")