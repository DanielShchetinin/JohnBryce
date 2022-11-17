number = int(input("Enter a 2-symbol number: "))
if number <= 9 or number > (99 + 1):
    print("Error, Try again")
    
symbol = number // 10
symbol2 = number % 10
symbol3 = symbol + symbol2
    
print(f"Your number is - {number} and sum of the 2 symbols is - {symbol3}") 