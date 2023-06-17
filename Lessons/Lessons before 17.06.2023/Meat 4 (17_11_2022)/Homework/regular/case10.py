various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
result = []

for i in various:
    if type(i) == int and i > 0:
        result.append(i)
        
print(various)
print(result)