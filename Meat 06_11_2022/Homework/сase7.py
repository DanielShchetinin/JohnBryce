def main():
    
    number = int(input("Enter a hundred number: "))
    if number < 100 or number > (999 + 1):
        print("\nError, please enter a hundred number again.\n")
        return main()
    
    print(f"\nNumber = {number}, The hundred number = {number // 100}")
    
if __name__ == '__main__':
    main()