import datetime

start = datetime.datetime.now()

num = 0
while True:
    print(num)
    num += 1
    if num == 100+1:
        break

end = datetime.datetime.now()
date = end.strftime("%d.%m.%Y")
time = end.strftime("%H:%M")
run_time = (end - start).total_seconds()
print("\nProgram Run Time:", run_time, "Seconds\n")
