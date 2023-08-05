from shapes.detect import *
from shapes.calc import *

def main():

    lengths_sides_list = [2,5,5]
    result_is_rectangle = is_rectangle(lengths_sides_list)
    result_is_square = is_square(lengths_sides_list)
    result_is_triangle = is_triangle(lengths_sides_list)
    if result_is_rectangle == True:
        figure = "Rectangle"
    if result_is_square == True:
        figure = "Square"
    if result_is_triangle == True:
        figure = "Triangle"
    else:
        figure = None
    print(f"\n"*3, "This figure is:", figure, "\n"*2)
    result_rectangle_area = rectangle_area(lengths_sides_list)
    result_square_area = square_area(lengths_sides_list)
    result_triangle_area = (lengths_sides_list)
    print()




if __name__ == '__main__':
    main()