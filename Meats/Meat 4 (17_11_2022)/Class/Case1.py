# grades = [99, 98, 97, 96, 50, 40, 30]

# for grade in grades:
#     if grade > 95:
#         print(grade)


# names = ['Daniel', 'Andrei', 'Moshe']
# grades = []
# for name in names:
#     grade = int(input(f"Insert a grade for {name}: "))
#     grades.append(grade)
# # print(f"The grade for {name} is - {grade}")
# for inx, name in enumerate(names):
#     print(f"Record number {inx}, The grade of {name} is {grades[inx]}")

# word = 'Daniel'
# for char in word:
#     print(char)

# r = range(5000)

# print(r)
# print(type(r))
# print(r[5:15])


# print(range(5, 10, 2))
# my_range = range(5, 10, 2)
# print(my_range)

# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']

# for i in range(len(cities)-1, -1,-1):
#     print(f"{countries[i]} - {cities[i]}")
    
    
nums = [54, -1, 56, 425, 5, 1444, 4134, 1, 46, 75, 34]
max_num = max(nums[0:2])
sec_max = min(nums[0:2])
for num in nums:
    if num < sec_max:
        continue
    if num > sec_max and num < max_num:
        sec_max = num
    if num > max_num:
        sec_max = max_num
        max_num = num
print(sec_max)
