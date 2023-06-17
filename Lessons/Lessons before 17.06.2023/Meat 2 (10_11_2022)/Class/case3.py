# Implement a code that receives the layout of the seats in the aircraft as letters and returns the layout as numbers. For example:
# ABC DEF => 3 3
# AB CDEF GH => 2 4 2
# You can assume that the maximum number of seat “batches” in any aircraft is 3.

text = input("Enter a text in format AB CDE FG: ")
text1 = text.split(" ")
print(len(text1[0],  text[2]))