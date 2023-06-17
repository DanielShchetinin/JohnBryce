import json
path = "C:\\Users\\d1175\\Documents\\GitHub\\JohnBryce\\Class_Meats\\Meat 14 (09_01_2023)\\Class\\data\\check.txt"

def write_to_file(user_points):
    with open(path, "w") as f:
        for user, points in user_points.items():
            f.write(f"{user}: {points}\n")

user_points = {}
 
user = "dantegos"
points = 0
user_points[user] = points

write_to_file(user_points)


def update_points(user, points, user_points):
    user_points[user] = points

def read_from_file():
    with open(path, "r") as f:
        user_points = {}
        for line in f:
            user, points = line.strip().split(": ")
            user_points[user] = int(points)
        return user_points

user_points = read_from_file()

user = "dantegos"
points = 2
update_points(user, points, user_points)

write_to_file(user_points)