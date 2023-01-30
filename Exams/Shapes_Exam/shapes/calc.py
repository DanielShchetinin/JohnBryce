
# This function get a list of lengths sides and return the area of rectangle.
def rectangle_area(lengths_sides_list: list) -> int:
    side_a = lengths_sides_list[0]
    return side_a*side_a

def rectangle_perimeter(lengths_sides_list: list) -> int:
    return sum(lengths_sides_list)
# This function get a list of lengths sides and return the area of square.
def square_area(lengths_sides_list: list) -> int:
    side_a = lengths_sides_list[0]
    side_b = lengths_sides_list[1]
    return side_a*side_b

def square_perimeter(lengths_sides_list: list) -> int:
    return sum(lengths_sides_list)

# This function get a list of lengths sides and return the area of triangle.
def triangle_area(lengths_sides_list: list) -> float or int:
    side_a = lengths_sides_list[0]
    side_b = lengths_sides_list[1]
    side_c = lengths_sides_list[2]
    semi_area = (side_a+side_b+side_c)/2
    area = (semi_area*((semi_area-side_a)*(semi_area-side_b)*(semi_area-side_c))) ** 0.5
    if type(area) is not float:
        return None
    return area

def triangle_perimeter(lengths_sides_list: list) -> int:
    return sum(lengths_sides_list)