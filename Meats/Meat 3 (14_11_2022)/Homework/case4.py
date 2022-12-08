# # Write a program that receives student names and their grades one by one. 
# # The program should continue running until the user inserts "$$$" to indicate end of input. 
# # After receiving "$$$", the program should print all the names of the students and amount of the names received. 
# # In addition the program should print an average grade.

error = 'Error, Please try again!'
students = []
grades = []
while True:
    student = input("Enter student name: ").title() 
    if student == '$$$':
        break
    if not student.isnumeric():
        students.append(student)
    else:
        print(error)
        continue
    
    while True:
        grade = input(f"Enter a grade for {student}: ")
        if grade.isnumeric():
            grade = int(grade)
            if grade < 0 or grade > 100:
                print(error)
                continue
            else:
                grades.append(grade)
                break
        print(error)
            
for i in range(len(student)):
    print(students[i], "-", grades[i])
print(f"Average of grades:", sum(grades) / len(grades))