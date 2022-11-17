# 1. Use a loop to display elements from a given list present at odd index positions.
# For example, for list:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Expected output is:
# 20 40 60 80 100



my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for element in my_list[1::2]:
    print(element)