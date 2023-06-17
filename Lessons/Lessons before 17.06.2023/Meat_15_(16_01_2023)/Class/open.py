path = "Class_Meats\\Meat_15_(16_01_2023)\\Class\\alice_in_wonderland.txt"

with open(path, 'r', encoding="utf-8") as fd:
    count = 0
    for line in fd:
        count += line.lower().count("alice")
    print(f"the name alice, counted: {count} times.")