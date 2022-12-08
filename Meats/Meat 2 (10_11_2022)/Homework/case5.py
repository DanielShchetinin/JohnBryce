numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ,'0']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

seats = input("Enter your seat number: ")
if seats[0] not in letters:
    print("Error1")
if seats[1] not in numbers:
    print("Error2")

layout = int(input("Choose a layout variant from next list:\
\n1. ABC-DEF\n2. ABC-DEFG-HIJ\n3. AB-CD-EF\n\nEnter your choose number: "))
if layout == 1:
    layoutChoose = 'ABC-DEF' 
if layout == 2:
    layoutChoose = 'ABC-DEFG-HIJ'
if layout == 3:
    layoutChoose = 'AB-CD-EF'
else:
    print("Error3")

if layout == 1 and seats[0] == 'A' or 'F':
    position = 'Window'
if layout == 1 and seats[0] == 'B' or 'E':
    position = 'Middle'
if layout == 1 and seats[0] == 'C' or 'D':
    position = 'Aisle'

if layout == 2 and seats[0] == 'A' or 'J':
    position = 'Window'
if layout == 2 and seats[0] == 'B' or 'E' or 'F' or 'I':
    position = 'Middle'
if layout == 2 and seats[0] == 'C' or 'D' or 'G' or 'H':
    position = 'Aisle'

if layout == 3 and seats[0] == 'A' or 'F':
    position = 'Window'
if layout == 3 and seats[0] == 'B' or 'C' or 'D' or 'E':
    position = 'Aisle'
    
print(f"\nYour information:\nYour entered number: {seats} and choosed layout: {layout}.\nYour row: {seats[1]} and seat: {seats[0]}.\nYour position: {position}.\n")