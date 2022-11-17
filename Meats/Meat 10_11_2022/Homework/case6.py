# After check some planes, This only latter used
active_latters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
error = 'Error'
# Seats input and latter error
seats = input("Enter your seats number: ")
seat_latter = None
seat_latter = seats[0]
seat_latter = seat_latter.upper()
if seat_latter not in active_latters:
    print(error)

# Seats number check and error
seats_count = len(seats)
seat_row = None
if seats_count == 2:
    seat_row = seats[1]
if seats_count == 3:
    seat_row = seats[1:2+1]
if seats_count <= 0 or seats_count >= 4 or seat_row == None:
    print(error)
else:
    seats_row = int(seat_row)

#Layout input and layout errors
layout = input("\nEnter your seats layout [Example: ABC DEFG HJK]\nInsert: ")
layout = layout.upper()
layout_list = layout.split(" ")
layout_count = len(layout_list)
if layout_count == 1 or layout_count >= 4:
    print(error)

#Plane Types
big_plane = 'Big Plane' # ABC DEFG HJK or ABC DEF GHJ
middle_plane = 'Middle Plane' # AB CDEF GH or ABC DEF or AB CD EF
small_plane = 'Small Plane' # AB CD or AB CDE
private_plane = 'Private Plane' # A B or A BC 

plane_type = None
if layout_count == 3 and len(layout_list[0]) == 3 and len(layout_list[1]) == 3 and len(layout_list[2]) == 3:
    plane_type = big_plane
if layout_count == 3 and len(layout_list[0]) == 3 and len(layout_list[1]) == 4 and len(layout_list[2]) == 3:
    plane_type = big_plane

if layout_count == 3 and len(layout_list[0]) == 2 and len(layout_list[1]) == 3 and len(layout_list[2]) == 2:
    plane_type = middle_plane
if layout_count == 3 and len(layout_list[0]) == 2 and len(layout_list[1]) == 4 and len(layout_list[2]) == 2:
    plane_type = middle_plane
if layout_count == 2 and len(layout_list[0]) == 3 and len(layout_list[1]) == 3:
    plane_type = middle_plane
if layout_count == 3 and len(layout_list[0]) == 2 and len(layout_list[1]) == 2 and len(layout_list[2]) == 2:
    plane_type = middle_plane
    
if layout_count == 2 and len(layout_list[0]) == 2 and len(layout_list[1]) == 2:
    plane_type = small_plane
if layout_count == 2 and len(layout_list[0]) == 2 and len(layout_list[1]) == 3:
    plane_type = small_plane
    
if layout_count == 2 and len(layout_list[0]) == 1 and len(layout_list[1]) == 1:
    plane_type = private_plane
if layout_count == 2 and len(layout_list[0]) == 1 and len(layout_list[1]) == 2:
    plane_type = private_plane


# Window or Middle or Aisle
pos_window = 'Window'
pos_middle = 'Middle'
pos_aisle = 'Aisle'
pos_window_aisle = 'Window and Aisle'

position = None # Static window
if plane_type != private_plane and seat_latter == layout[0] or seat_latter == layout[-1]:
    position = pos_window
    
# ABC DEFG HJK or ABC DEF GHJ
elif plane_type == big_plane and len(layout_list[1]) == 3 and (seat_latter == layout[1] or seat_latter == layout[5] or seat_latter == layout[-2]):
    position = pos_middle
elif plane_type == big_plane and len(layout_list[1]) == 4 and (seat_latter == layout[1] or seat_latter == layout[6] or seat_latter == layout[-2]):
    position = pos_middle
elif plane_type == big_plane and len(layout_list[1]) == 3 and (seat_latter == layout[2] or seat_latter == layout[4] or seat_latter == layout[6] or seat_latter == layout[-3]):
    position = pos_aisle
elif plane_type == big_plane and len(layout_list[1]) == 4 and (seat_latter == layout[2] or seat_latter == layout[4] or seat_latter == layout[7] or seat_latter == layout[-3]):
    position = pos_aisle

# AB CDEF GH or ABC DEF or AB CD EF
elif plane_type == middle_plane and len(layout_list[1]) == 4 and seat_latter == layout[1] or seat_latter == layout[-2] or seat_latter == layout[4] or seat_latter == layout[6]:
    position = pos_aisle
elif plane_type == middle_plane and len(layout_list[1]) == 3 and seat_latter == layout[2] or seat_latter == layout[-3]:
    position = pos_aisle
elif plane_type == middle_plane and len(layout_list[1]) == 2 and seat_latter == layout[1]  or seat_latter == layout[3] or seat_latter == layout[4] or seat_latter == layout[-2]:
    position = pos_aisle
elif plane_type == middle_plane and len(layout_list[1]) == 4 and seat_latter == layout[4]  or seat_latter == layout[5]:
    position = pos_middle
elif plane_type == middle_plane and len(layout_list[1]) == 3 and seat_latter == layout[1]  or seat_latter == layout[-2]:
    position = pos_middle

# AB CD or AB CDE
elif plane_type == small_plane and len(layout_list[1]) == 2 and seat_latter == layout[1] or seat_latter == layout[3]:
    position = pos_aisle
elif plane_type == small_plane and len(layout_list[1]) == 3 and seat_latter == layout[1] or seat_latter == layout[3]:
    position = pos_aisle
elif plane_type == small_plane and len(layout_list[1]) == 3 and seat_latter == layout[-2]:
    position = pos_middle

# A B or A BC
elif plane_type == private_plane and len(layout_list[1]) == 1 and seat_latter == layout[0] or seat_latter == layout[2]:
    position = pos_window_aisle
elif plane_type == private_plane and len(layout_list[1]) == 2 and seat_latter == layout[0]:
    position = pos_window_aisle
elif plane_type == private_plane and len(layout_list[1]) == 2 and seat_latter == layout[-1]:
    position = pos_window
elif plane_type == private_plane and len(layout_list[1]) == 2 and seat_latter == layout[-2]:
    position = pos_aisle
    
else: 
    print(error)
    plane_type = "SEAT ERROR"


# Info
print("\n\n\n\n\n\nYour ticket information:\n")
print(f"You enter: {layout} and {seats}")
print(f"Your plane type: {plane_type}.")
print(f"Your seat: row {seat_row} and chair {seat_latter}.")
print(f"Your posistion: {position}")