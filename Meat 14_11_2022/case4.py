airplane = input("Please enter symbols in next format\nAB CDE FG\nInsert: ")
text = airplane.split(" ")
text1 = len(airplane.split()[0])
text2 = len(airplane.split()[1])
text3 = len(airplane.split()[2])

print(f"{text1} {text2} {text3}")