
# We get a number from user
movie_num = int(input("Enter your minutes: "))

# Calc the hours and minutes of the movie
hours = movie_num // 60
minutes = movie_num % 60

# Send a result
print(f"Your movie is {hours} hours and {minutes} minutes")