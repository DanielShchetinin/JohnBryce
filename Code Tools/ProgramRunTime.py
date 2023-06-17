import datetime

start = datetime.datetime.now()
end = datetime.datetime.now()
date = end.strftime("%d.%m.%Y")
time = end.strftime("%H:%M")
run_time = (end - start).total_seconds()
print("\nProgram Run Time:", run_time, "Seconds\n")