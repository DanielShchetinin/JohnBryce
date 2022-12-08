birthdays = {}
while True:
    doing = input("Enter what you want to do (Insert / Lookup / Exit): ")

    if doing == "Insert":
        while True:
            name = input("Enter a name: ")
            if name == '$':
                break
            date = input("Enter a date: ")
            birthdays[name] = date

    if doing == "Lookup":
        while True:
            lookup = input("Enter a name to get a date: ")
            if lookup == '$':
                break
            if lookup not in birthdays:
                print("Error, Try again")
                continue
            print(birthdays.get(lookup, 'Sorry we dont have this name!'))
    
    if doing == 'Exit':
        break