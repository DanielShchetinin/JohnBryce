error = "Error, Please, Try again!"

while True:

    rows = input("Enter how much row you want: ")
    if not rows.isnumeric():
        print(error)
        continue
    columns = input("Enter how much row you want: ")
    if not columns.isnumeric():
        print(error)
        continue
    else:
        break
    
rows = int(rows)
columns = int(columns)

for i in range(columns):
    print("$"*rows)