from detect import *
from calc import *

shapes=[[2, 2, 2, 2], [3, 4, 5], [5, 6, 6], [2, 3, 2, 3], [2, 3, 8], [3, 4, 5]] 
complete_shapes = {}
used_shapes = []
unused_shapes = []
sorted_shapes_list = []

rectangles_list = []
squares_list = []
triangles_list = []

for shape in shapes:
    if shape in used_shapes:
        continue
    sorted_shape = shape.sort()
    for sort_shape in sorted_shapes_list:
        if sorted_shape == sort_shape:
            sorted_shapes_list.append(sorted_shape)
    used_shapes.append(shape)
    
    lengths_sides_list = shape

    result = is_rectangle(lengths_sides_list)
    if result == True:
        rectangle_area_result = rectangle_area(lengths_sides_list)
        rectangle_perimeter_result = rectangle_area(lengths_sides_list)
        rectangles_list.append([{"sides": shape,\
        "area":rectangle_area_result,\
        "perimeter":rectangle_perimeter_result}])

    result = is_square(lengths_sides_list)
    if result == True:
        square_area_result = square_area(lengths_sides_list)
        square_perimeter_result = square_perimeter(lengths_sides_list)
        squares_list.append({"sides": shape,\
        "area":square_area_result,\
        "perimeter":square_perimeter_result})

    result = is_triangle(lengths_sides_list)
    if result == True:
        triangle_area_result = triangle_area(lengths_sides_list)
        triangle_perimeter_result = triangle_area(lengths_sides_list)
        triangles_list.append({"sides": shape,\
        "area":triangle_area_result,\
        "perimeter":triangle_perimeter_result})

complete_shapes["rectangle"] = rectangles_list
complete_shapes["squares"] = squares_list
complete_shapes["triangels"] = triangles_list

print(complete_shapes)
print("\n")
print(unused_shapes)
print("\n")
print(sorted_shapes_list)
