def main():
    
    Number = int(input("Enter a number between 1000 to 9999: "))
    if Number > 10000 or Number < 1000:
        print("\nError: Your enter a wrong number, Please try again.\n")
        return main()
    print(f"You choose {Number} Your right digit is {Number % 20}")

if __name__ == '__main__':
    main()