# This function get a list of lengths sides and return if its can be a rectangle of not.
def is_rectangle(lengths_sides_list):
    if len(lengths_sides_list) == 4:
        if lengths_sides_list[0] != lengths_sides_list[1]:
            if lengths_sides_list[0] == lengths_sides_list[3] and lengths_sides_list[1] == lengths_sides_list[2]\
                or lengths_sides_list[0] == lengths_sides_list[2] and lengths_sides_list[1] == lengths_sides_list[3]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
# This function get a list of lengths sides and return if its can be a square of not.
def is_square(lengths_sides_list):
    if len(lengths_sides_list) == 4:
        if lengths_sides_list[0] == lengths_sides_list[1] == lengths_sides_list[2] == lengths_sides_list[3]:
            return True
        else:
            return False
    else:
        return False
# This function get a list of lengths sides and return if its can be a triangle of not.
def is_triangle(lengths_sides_list):
    if len(lengths_sides_list) == 3:
        side_a = lengths_sides_list[0]
        side_b = lengths_sides_list[1]
        side_c = lengths_sides_list[2]
        if (side_a + side_b) < side_c:
            return False
        if (side_a + side_b) > side_c:
            return True
        else:
            return False
    else:
        return False

